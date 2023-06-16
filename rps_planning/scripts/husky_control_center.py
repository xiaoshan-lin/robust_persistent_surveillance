#!/usr/bin/env python2.7

import rospy
import tf
import time
import sys, os
from std_msgs.msg import Bool
from geometry_msgs.msg import PoseStamped, PointStamped
from actionlib_msgs.msg import GoalStatusArray
from move_base_msgs.msg import MoveBaseActionFeedback
from numpy import remainder as rem
import numpy as np
from rps_msgs.msg import floatlist
from math import floor, ceil
import json
from rps_planning.srv import *

project_dir = os.path.abspath(__file__ + "/../../resource") 
PI = 3.1415926 

class Husky:

    def __init__(self, uav0, uav1, uav2, uav3):
        self.UAV_has_landed = True # landing flag for all UAVs
        self.UAV_has_landed_0 = False # flag for UAV 0
        self.UAV_has_landed_1 = False # flag for UAV 1
        self.UAV_has_landed_2 = False # flag for UAV 2
        self.UAV_has_landed_3 = False # flag for UAV 3
        self.UGV_has_arrived = True # goal-reaching flag for UGV
        self.UGV_has_arrived_next = False # auxiliary Goal-reaching flag for UGV
        self.husky_c_orien = [] # real-time orientation of UGV
        self.husky_c_pst = [] # real-time position of UGV
        self.sensing_range = 5.5 # sensing range of the laser
        self.msg2UAV = floatlist() # message to UAVs
        self.max_duration = rospy.get_rostime() - rospy.get_rostime() # maximum UAV flying duration
        self.has_updated = False # true if UGV has started updated information about obstacles
        self.unknown_options = [] # list of locations about which the UGV has no knowledge
        self.known_options = [] # list of non-obstacle locations known to the UGV
        self.known_obstacle = []# list of obstacles known to the UGV
        self.obstacles = [] # list of all obstacles
        self.goal=[] # (x,y) goal of the UGV
        self.period = 1200 # supercycle period
        self.ugv_idx = [] # ugv index 0,1,2,...,Num_ugv-1
        self.x_offset = 0
        self.y_offset = 0

        # goal topic for UGV
        self.husky_target_pub = rospy.Publisher('move_base_simple/goal', \
                PoseStamped, queue_size=10)

        # message topic from UGV to UAV
        self.cmd2UAV_pub = rospy.Publisher('cmd2UAV', floatlist, queue_size=10)

        # message topic from UAV0 to UGV
        self.cmd2UGV_sub_0 = rospy.Subscriber('/hummingbird' + uav0 + '/cmd2UGV',\
                       Bool, self.cmd2UGV_callback_0)
  
        # message topic from UAV1 to UGV
        self.cmd2UGV_sub_1 = rospy.Subscriber('/hummingbird' + uav1 + '/cmd2UGV',\
                Bool, self.cmd2UGV_callback_1)

        # message topic from UAV2 to UGV
        self.cmd2UGV_sub_2 = rospy.Subscriber('/hummingbird' + uav2 + '/cmd2UGV',\
                       Bool, self.cmd2UGV_callback_2)

        # message topic from UAV3 to UGV
        self.cmd2UGV_sub_3 = rospy.Subscriber('/hummingbird' + uav3 + '/cmd2UGV',\
                       Bool, self.cmd2UGV_callback_3)

        # UGV real-time pose topic from the navigation stack
        self.husky_state_sub = rospy.Subscriber('move_base/feedback',\
                       MoveBaseActionFeedback, self.husky_state_callback)

        # navigation status        
        self.UGV_status_sub = rospy.Subscriber('move_base/status',GoalStatusArray,\
                            self.UGV_status_callback)

    def husky_target_publisher(self,husky_pose,ns):
        # publish UGV goal to move_base node
        pose = PoseStamped()
        pose.header.frame_id=self.header
        pose.header.stamp = rospy.Time.now()
        pose.pose.position.x = husky_pose['x'] - self.x_offset
        pose.pose.position.y = husky_pose['y'] - self.y_offset
        pose.pose.position.z = husky_pose['z']   

        if type(husky_pose['yaw'])==float:
            quaternion = tf.transformations.quaternion_from_euler(0,0,husky_pose['yaw'])            
            pose.pose.orientation.x = quaternion[0]
            pose.pose.orientation.y = quaternion[1]
            pose.pose.orientation.z = quaternion[2]
            pose.pose.orientation.w = quaternion[3]
        elif type(husky_pose['yaw']) == list:
            quaternion = husky_pose['yaw']          
            pose.pose.orientation.x = quaternion[0]
            pose.pose.orientation.y = quaternion[1]
            pose.pose.orientation.z = quaternion[2]
            pose.pose.orientation.w = quaternion[3]
        
        for i in range(5):
            rospy.loginfo("----Publishing target msgs to UGV----")
            self.husky_target_pub.publish(pose)
            time.sleep(0.05)

    def cmd2UGV_callback_0(self,data):
        rospy.loginfo('listening to UAV')
        self.UAV_has_landed_0 = data.data
    
    def cmd2UGV_callback_1(self,data):
        rospy.loginfo('listening to UAV')
        self.UAV_has_landed_1 = data.data
    
    def cmd2UGV_callback_2(self,data):
        rospy.loginfo('listening to UAV')
        self.UAV_has_landed_2 = data.data

    def cmd2UGV_callback_3(self,data):
        rospy.loginfo('listening to UAV')
        self.UAV_has_landed_3 = data.data

    def UGV_status_callback(self, data):        
        if data.status_list == [] or data.status_list[0].status != 3:    
            self.UGV_has_arrived_next = False
        elif data.status_list[0].status == 3:
            current_p = self.husky_c_pst
            if abs(current_p.x-husky.goal[0])<0.3 and abs(current_p.y-husky.goal[1])<0.3:
                self.UGV_has_arrived_next = True 
    
    def husky_state_callback(self,data):
        self.husky_c_orien = data.feedback.base_position.pose.orientation
        self.husky_c_pst = data.feedback.base_position.pose.position 
        self.husky_c_pst.x += self.x_offset 
        self.husky_c_pst.y += self.y_offset

    def check_UAV_status(self):
        # check if all UAVs has landed on the UGV
        if self.UAV_has_landed_0 and self.UAV_has_landed_1 and \
           self.UAV_has_landed_2  and self.UAV_has_landed_3:
            self.UAV_has_landed = True
        else:
            self.UAV_has_landed = False

if __name__ == '__main__':
    
    try:
        rospy.init_node('husky_control_center', anonymous=True)
        rospy.loginfo_once('------husky_control_center launched successfully!------')
        rospy.wait_for_service('/age_server')
        send_timelist = rospy.ServiceProxy('/age_server', age)       
           
        rate = rospy.Rate(5)
        
        uav0 = sys.argv[3]
        uav1 = sys.argv[4]
        uav2 = sys.argv[5]
        uav3 = sys.argv[6]       
        
        husky=Husky(uav0,uav1,uav2,uav3)
        husky.ns = sys.argv[2]
        husky.ugv_idx = int(sys.argv[7])
        
        # turtlebot is based on turtlebot/odom frame, whose origin is at the initial position of the ugv
        # the following code is used to get the translation from odom frame to world frame (turtlebot)
        if husky.ns[0:5] == "husky":
            husky.header = 'world'
            husky.x_offset = 0.0
            husky.y_offset = 0.0
        elif husky.ns[0:5] == "turtl":
            husky.header = husky.ns+'/odom'
            husky.x_offset = float(sys.argv[8])
            husky.y_offset = float(sys.argv[9])
        else:
            print("ugv name not recognized, please check your sim.launch file")
            raise

        husky_x = []
        husky_y = []

        '''get offline ugv plan
        heading_idx (UGV): 0(heading to +x axis)
                           1(heading to +y axis)
                           2(heading to -x axis)
                           3(heading to -y axis)'''    
        husky_pose = []        
        heading_idx = []
        f=np.load(os.path.join(project_dir,'ugvwaypoint.npz'), 'rb')
        husky_pose_=f['pos']
        dist_btw_pose=f['delta']
        robust = f['robust'] 
        size = husky_pose_.shape[1] 
        for i in range(size):
            if husky_pose_[0][i]==husky_pose_[0][i-1]:
                if husky_pose_[1][i]>husky_pose_[1][i-1]:
                    husky_yaw = 3.14159/2
                    heading_idx.append(1)
                else:
                    husky_yaw = 3*3.14159/2
                    heading_idx.append(3) 
            elif husky_pose_[1][i]==husky_pose_[1][i-1]:
                if husky_pose_[0][i]>husky_pose_[0][i-1]: 
                    husky_yaw = 0.0
                    heading_idx.append(0)
                else:
                    husky_yaw = 3.14159
                    heading_idx.append(2)
            else:
                if husky_pose_[1][i]>husky_pose_[1][i-1] and husky_pose_[0][i]>husky_pose_[0][i-1]:
                    husky_yaw = 3.14159/4
                    heading_idx.append(1)
                elif husky_pose_[1][i]>husky_pose_[1][i-1] and husky_pose_[0][i]<husky_pose_[0][i-1]:
                    husky_yaw = 3*3.14159/4
                    heading_idx.append(2)
                elif husky_pose_[1][i]<husky_pose_[1][i-1] and husky_pose_[0][i]>husky_pose_[0][i-1]:
                    husky_yaw =7*3.14159/4
                    heading_idx.append(0)
                else:
                    husky_yaw =5*3.14159/4
                    heading_idx.append(3)
            
            husky_pose.append({'x':husky_pose_[0][i],\
                    'y':husky_pose_[1][i],\
                    'z':0,\
                    'yaw':husky_yaw})
        
        with open(os.path.join(project_dir,'data.json'), 'r') as f:
            info = json.load(f) 

        idx = int(sys.argv[1])
        ns = sys.argv[2] # node namespace
        stage = 0 # 0: send ugv goal; 1: wait for ugv reach goal; 2: wait for uav to land
        pt_f = 0 # print flag
        takeoff_time = 0 # uav start time
        setoff_time = 0 # ugv start time
        has_arrived = 0 # counter 
        pre_time = None # start time of the pervious cycle       
        time_list = [[] for j in range(5)]
        cycle_idx = -1 # supercycle index
        init_time = rospy.get_time()

        # list of alternative location when release point is blocked
        alternative = [(x,y) for x in range(-1*robust,robust+1) for y in range(-1*robust,robust+1)]
        remove_id = []
        for index,val in enumerate(alternative):
            if val[0]**2+val[1]**2>robust**2:
                remove_id.append(index)
        for index in sorted(remove_id, reverse=True):
            del alternative[index]

        # obstacle coordinates
        husky.obstacles = [(0.50,1.50),(1.50,1.50),(2.50,1.50),(4.50,11.5),(4.50,12.5),(4.50,13.5),(2.50,24.5),\
                           (3.50,24.5),(4.50,24.5),(5.50,24.5),(6.50,24.5),(22.5,21.5),(21.5,20.5),(21.5,21.5),\
                           (21.5,22.5),(24.5,2.50),(24.5,3.50),(24.5,4.50),(24.5,5.50),(24.5,6.50),(24.5,7.50),\
                           (24.5,8.50),(24.5,9.50),(24.5,0.50),(24.5,1.50),(7.50,3.50),(8.50,3.50),(9.50,2.50),\
                           (7.50,7.50),(7.50,8.50),(8.50,7.50),(8.50,8.50),(5.50,18.5),(6.50,18.5),(7.50,18.5),\
                           (8.50,18.5),(5.50,19.5),(7.50,19.5),(12.5,17.5),(12.5,15.5),(15.5,9.50),(16.5,8.50),\
                           (17.5,6.50),(17.5,7.50),(17.5,8.50),(18.5,4.50),(4.50,20.5),(4.50,21.5),(20.5,21.5),\
                           (20.5,20.5),(20.5,13.5),(21.5,13.5),(21.5,12.5),(20.5,12.5),(13.5,4.5)]
        rospy.sleep(rospy.Duration(1))
 
        if husky.ugv_idx>0:
            stage = -1
        one_time_flag = True

        while not rospy.is_shutdown():

            # for the second ugv, stop for a few seconds and then start
            if stage == -1:                
                rospy.sleep(rospy.Duration(160)) 
                stage = 0
                 
            if stage == 0:
                if husky.husky_target_pub.get_num_connections()<1:
                    pass
                else:
                    setoff_time = rospy.get_rostime()
                    if pt_f == 0:
                        rospy.loginfo("Sending UGV target")                                             
                        pt_f = pt_f+1
                    if husky.UAV_has_landed and husky.UGV_has_arrived:
                        idx = rem(idx+1,len(husky_pose))
                        
                        if idx == 0:
                            cycle_idx += 1
                            send_flag = True
                            start_time = rospy.get_time()
                            if pre_time != None:
                                rospy.loginfo("**********Cycle***********")
                                cycle = start_time - pre_time
                                print('Previous cycle time:{}'.format(cycle))
                            pre_time = start_time
                           
                        area_type = info[str(idx)]                      
                            
                        husky.husky_target_publisher(husky_pose[idx],ns)
                        husky.goal=[husky_pose[idx]['x'],husky_pose[idx]['y']]
                        print('UGV target pose (x,y,z,yaw):{},{},{},{}'.format(
                            husky_pose[idx]['x'],husky_pose[idx]['y'],\
                                    husky_pose[idx]['z'],husky_pose[idx]['yaw']))
                        time.sleep(1)
                        husky.UGV_has_arrived = False
                        husky.UGV_has_arrived_next = False
                        stage = 1
                        
            elif stage == 1:
                if pt_f == 1:
                    rospy.loginfo("Waiting for UGV to arrive")
                    time.sleep(1)
                    pt_f=pt_f+1
                
                # update information about the robust region
                cpst = husky.husky_c_pst   
                if cycle_idx == 0:
                    husky_x.append(cpst.x) 
                    husky_y.append(cpst.y)           
                if (husky_pose[idx]['x']-cpst.x)**2+\
                (husky_pose[idx]['y']-cpst.y)**2 < (robust+husky.sensing_range)**2:
                    right=floor(cpst.x+husky.sensing_range+0.5)-0.5
                    left=ceil(cpst.x-husky.sensing_range+0.5)-0.5
                    up=floor(cpst.y+husky.sensing_range+0.5)-0.5
                    down=ceil(cpst.y-husky.sensing_range+0.5)-0.5

                    check_xy = [(check_x, check_y) for check_x in np.arange(left,right+0.1) \
                                                   for check_y in np.arange(down,up+0.1)]
                    """print 'check_xy'
                    print check_xy
                    print '\n' """
                    
                    if husky.unknown_options == [] and not husky.has_updated:
                        husky.unknown_options = [(husky_pose[idx]['x']+i[0],\
                                            husky_pose[idx]['y']+i[1]) for i in alternative]
                        """print 'unknown options'
                        print(husky.unknown_options)
                        print '\n' """
                    else: 
                        husky.has_updated = True
                        remove_xy = []
                        for i in check_xy:
                            if i in husky.unknown_options and \
                                (i[0]-cpst.x)**2+(i[1]-cpst.y)**2 <= husky.sensing_range**2:
                                rospy.loginfo("----Updating environment----")
                                if i in husky.obstacles:
                                    husky.known_obstacle.append(i)
                                    remove_xy.append(i)
                                else:
                                    potential_blocked = [(i[0]+b_x,i[1]+b_y) for b_x in [-1,0,1] for b_y in [-1,0,1]]
                                    if sum([p in husky.obstacles for p in potential_blocked]) == 0:
                                        husky.known_options.append(i)
                                    else:
                                        husky.known_obstacle.append(i)                                  
                                    remove_xy.append(i)
                        """print 'known obstacles'
                        print husky.known_obstacle
                        print '\n'
                        print 'known options'
                        print husky.known_options
                        print '\n'"""
                        for i in remove_xy:
                            husky.unknown_options.remove(i)  
                        remove_xy = []                                          
                
                # goal is blocked by obstacles, search for nearest feasible point
                if (husky_pose[idx]['x'],husky_pose[idx]['y']) in husky.known_obstacle:                   
                    cpot=husky.husky_c_pst
                    corien=husky.husky_c_orien
                    nearest=0
                    dist=10000
                    
                    if husky.known_options != []:
                        for index,val in enumerate(husky.known_options):   
                            dist_new = (val[0]-cpot.x)**2+(val[1]-cpot.y)**2
                            if dist_new < dist:
                                dist = dist_new
                                x_new = val[0]
                                y_new = val[1]

                    else:
                        for index,val in enumerate(alternative):   
                            dist_new = (husky_pose[idx]['x']+val[0]-cpot.x)**2+\
                            (husky_pose[idx]['y']+val[1]-cpot.y)**2
                            if dist_new < dist:
                                   nearest = index
                                   dist = dist_new
                        x_new = husky_pose[idx]['x']+alternative[nearest][0]
                        y_new = husky_pose[idx]['y']+alternative[nearest][1]

                    qua = [corien.x,corien.y,corien.z,corien.w] 
                    #yaw_new = tf.transformations.euler_from_quaternion(qua)[2]                   
                    husky_pose_new = {'x':x_new,\
                                      'y':y_new,\
                                      'z':0,\
                                      'yaw':husky_pose[idx]['yaw']}
                    husky.husky_target_publisher(husky_pose_new, ns)
                    husky_pose[idx] = husky_pose_new
                    husky.goal=[husky_pose[idx]['x'],husky_pose[idx]['y']]

                    rospy.loginfo("Sending new targets to UGV")
                    print('UGV target pose (x,y,z,yaw):{},{},{},{}'.format(
                                husky_pose_new['x'],husky_pose_new['y'],\
                                husky_pose_new['z'],husky_pose_new['yaw']))
                    rospy.sleep(rospy.Duration(1))
                    
                if husky.UGV_has_arrived_next == True:
                    husky.known_options = []
                    husky.unknown_options = []
                    husky.has_updated = False
                    rospy.loginfo('Goal reached')
                    has_arrived = has_arrived + 1
                    husky_qua =  [husky.husky_c_orien.x, husky.husky_c_orien.y,\
                                  husky.husky_c_orien.z, husky.husky_c_orien.w]
                    yaw = tf.transformations.euler_from_quaternion(husky_qua)[2]

                    rospy.loginfo('Distance to goal:')
                    dist_yaw = abs(yaw-husky_pose[idx]['yaw'])
                    if dist_yaw > PI:
                        dist_yaw = 2*PI-dist_yaw
                    dist_x = abs(husky.husky_c_pst.x-husky_pose[idx]['x'])
                    dist_y = abs(husky.husky_c_pst.y-husky_pose[idx]['y'])
                    dist_z = abs(husky.husky_c_pst.z-husky_pose[idx]['z'])

                    condition = int(dist_x < 0.25) + int(dist_y<0.25) + int(dist_yaw<0.25) + int(has_arrived>12)
                                     
                    if condition >= 3:
                        has_arrived = 0
                        rospy.loginfo('UGV has arrived!')                       
                        UGV_duration = rospy.get_rostime()-setoff_time
                        if UGV_duration < husky.max_duration:
                            rospy.loginfo('Waiting for UAV to get charged!')
                            #print(husky.max_duration.to_sec())
                            #print(UGV_duration.to_sec())
                            #print(husky.max_duration-UGV_duration)
                            rospy.sleep(husky.max_duration-UGV_duration)
                        time_list[cycle_idx].append(rospy.get_time() - init_time)
                        husky.UAV_has_landed = False
                        husky.msg2UAV.type = area_type
                        husky.msg2UAV.x=dist_btw_pose[0][idx]
                        husky.msg2UAV.y=dist_btw_pose[1][idx]
                        
                        husky.msg2UAV.idx=heading_idx[idx]
                        if husky.ugv_idx>0 and cycle_idx==0 and idx==0 and one_time_flag:
                            rospy.sleep(rospy.Duration(husky.period/2-rospy.get_time()+init_time))
                            one_time_flag = False
                        for i in range(1):
                            husky.cmd2UAV_pub.publish(husky.msg2UAV)
                            rospy.loginfo_once("Publishing cmd to UAV")
                            time.sleep(0.1)
                        stage = 2
                        takeoff_time = rospy.get_rostime()
            
            elif stage ==2:
                if pt_f == 2:
                    rospy.loginfo("Waiting for UAV to land")
                    husky.UAV_has_landed_0 = False 
                    husky.UAV_has_landed_1 = False
                    pt_f=0
                husky.check_UAV_status()
                if husky.UAV_has_landed == True:
                    husky.max_duration = rospy.get_rostime() - takeoff_time
                    husky.UGV_has_arrived = True
                    stage = 0

            if len(time_list[cycle_idx]) == len(husky_pose) and send_flag:
                timelist_flag = send_timelist(time_list[cycle_idx])
                if timelist_flag == True:
                    print("Sent time list successfully")
                send_flag = False
            rate.sleep()

    except rospy.ROSInterruptException:
        for idx,i in enumerate(time_list):
            if len(i) < len(husky_pose):
                break
        if idx>0:
            time_array = np.array(time_list[0:idx])
            time_interval = time_array[1:,:]-time_array[0:idx-1,:]
            age = max(time_interval.max(axis=0))

        print("age from {} is {}".format(ns, age))
        np.save(os.path.join(project_dir,'trajectory.npy'),np.array([husky_x,husky_y]))
            
