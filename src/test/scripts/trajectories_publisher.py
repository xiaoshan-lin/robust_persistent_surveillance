from __future__ import print_function

import rospy
from std_msgs.msg import String, duration
from geometry_msgs.msg import Pose, Twist
from quadrotor_msgs.msg import Trajectory
from quadrotor_msgs.msg import TrajectoryPoint
import numpy as np

reference_trajectory=Trajectory()
point=TrajectoryPoint()
pose=Pose()
velocity=Twist()
acceleration=Twist()
jerk=Twist()
snap=Twist()


pose.orientation.w=1
pose.orientation.x=0
pose.orientation.y=0
pose.orientation.z=0

trajectories=np.array([[2,2,4,0],[0,2,4,4],[2,2,2,2]])

reorder=list(range(1,trajectories.shape[1]))+[0]
distance=np.sqrt(sum(np.square(trajectories-trajectories[:,reorder])))
time_stamp=np.cumsum(distance)/v_max


for t in trajectories.shape[1]:
    point

def talker():
    pub = rospy.Publisher('reference_trajectory', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    i=0
    while not rospy.is_shutdown():
        if i<10:
            hello_str = "hello world %s" % rospy.get_time()
            rospy.loginfo(hello_str)
            pub.publish(hello_str)
            rate.sleep()
            i=i+1
        else:
            break
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
