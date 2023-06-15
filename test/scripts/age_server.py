#!/usr/bin/env python2.7
import os
import rospy
from test.srv import age, ageResponse
import numpy as np
project_dir = os.path.abspath(__file__ + "/../../resource") 
f=np.load(os.path.join(project_dir,'ugvwaypoint.npz'), 'rb')
husky_pose_=f['pos']
num = husky_pose_.shape[1]

class ageServer:
    def __init__(self):
        self.timelist = []
        rospy.init_node('age_server_node')
        s = rospy.Service('age_server', age, self.handle_timelist)
        print("Ready to receive time list")

    def handle_timelist(self,req):
        self.timelist.append(list(req.data))
        
        print("----Received time list----")
        return ageResponse(True)
  
if __name__ == "__main__":
    AgeServer = ageServer()
    try:
        while not rospy.is_shutdown():
            pass
    except rospy.ROSInterruptException:
        time_list = AgeServer.timelist
        print(time_list)
        for idx,i in enumerate(time_list):
            if len(i) < num:
                break
        if idx>0:
            time_array = np.array(time_list[0:idx])
            time_interval = time_array[1:,:]-time_array[0:idx-1,:]
            age = max(time_interval.max(axis=0))

        print("age from {} is {}".format(ns, age))

