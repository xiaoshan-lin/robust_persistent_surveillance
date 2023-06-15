#!/usr/bin/env python2.7

import rospy
import time
from std_msgs.msg import Int8, Bool
from geometry_msgs.msg import PointStamped

class UAV:

    def __init__(self):

        self.ns = rospy.get_namespace()
        self.position = []
        self.last_position = []
        self.is_stop = Bool()
        self.is_stop.data = True
        self.not_stop = Bool()
        self.not_stop.data = False


        self.sub=rospy.Subscriber("ground_truth/position", PointStamped, self.positionCallback) 
        #rospy.Subscriber("cmd2UAV", Int8, cmd2UAVCallback)

        self.UAV_state_pub = rospy.Publisher("UAV_is_stop", Bool, queue_size=5) 
        #turn_off_motor_pub = rospy.Publisher("turnoffmotor", Bool, queue_size=1)
        #cmd2UGV_pub = rospy.Publisher("cmd2UGV", Bool, queue_size=1)

    def UAV_state_publisher(self):
        if self.position != []:
            l_p = self.position
            time.sleep(0.1)
            c_p = self.position
            if abs(c_p.x-l_p.x)<0.005 and abs(c_p.y-l_p.y)<0.005 \
                    and abs(c_p.z-l_p.z)<0.005:
                self.UAV_state_pub.publish(self.is_stop)

            else:
                self.UAV_state_pub.publish(self.not_stop)


    def positionCallback(self,data):
        self.position=data.point
               
        
if __name__ == "__main__":
    rospy.init_node('uavState', anonymous=True)
    uav=UAV()
    rospy.loginfo_once(uav.ns+"uavStatePublisher has launched")
    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
        uav.UAV_state_publisher()
        rate.sleep()
        
        



 

