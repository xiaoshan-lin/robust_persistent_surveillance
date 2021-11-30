#ifndef UAV_CONTROL_CENTER_H
#define UAV_CONTROL_CENTER_H

#include <fstream>
#include <iostream>
#include <ros/ros.h>
#include <trajectory_msgs/MultiDOFJointTrajectory.h>
#include <waypointstruct.h>
#include <geometry_msgs/Point.h>
#include <geometry_msgs/PointStamped.h>
#include <test_msgs/floatlist.h>
#include <std_msgs/Bool.h>
#include <std_msgs/Empty.h>
#include <quadrotor_msgs/Trajectory.h>
#include <quadrotor_msgs/TrajectoryPoint.h>
#include <geometry_msgs/Pose.h>
#include <tf2/LinearMath/Quaternion.h>
#include <tf2_geometry_msgs/tf2_geometry_msgs.h>

namespace rotors_gazebo {

class UAV_CONTROL_CENTER {
 public:
 
  bool is_stop;
  double ave_vel;
  double sample_rate;
  
  geometry_msgs::Point pt;
  quadrotor_msgs::TrajectoryPoint empty_point;
   
  struct X{
  int type = 4;
  double x;
  double y;
  int heading_idx;
  };

  X flight_info;

  UAV_CONTROL_CENTER(const ros::NodeHandle& nh, const ros::NodeHandle& private_nh);
  ~UAV_CONTROL_CENTER();

  void InitializeParams();

  int uav_trajectory_publisher(std::vector<waypointstruct>&new_waypoints, double disp_x, double disp_y);

  void bridge_publisher();
 
  void hover_publisher();

  ros::Publisher turnoffmotor_pub;
  ros::Publisher cmd2UGV_pub;
  ros::Publisher chatter_pub;

 private:

  double a_x, b_x, c_x, d_x, a_y, b_y, c_y, d_y, a_z, b_z, c_z, d_z;  
  double last_x;
  double last_y;
  double last_z;
  double x;
  double y;
  double z;
  double yaw;
  double x_next;
  double y_next;
  double z_next;
  double yaw_next;
  double dist2next;
  double t2next;

  ros::NodeHandle nh_;
  ros::NodeHandle private_nh_;

  std::string namespace_;

  ros::Publisher trajectory_pub; 
  ros::Publisher bridge_pub;
  ros::Publisher hover_pub;

  ros::Subscriber cmd2UAV_sub;
  ros::Subscriber UAVstate_sub;
  ros::Subscriber UAVpos_sub;
  ros::Subscriber status_sub;

  quadrotor_msgs::Trajectory trajectory;
  quadrotor_msgs::TrajectoryPoint trajectory_point;
  double len_from_start = 0;
  float t_from_start = 0;
  ros::Duration time_from_start;
  geometry_msgs::Pose pose;
  tf2::Quaternion myQuaternion;
  geometry_msgs::Quaternion orientation;
  std_msgs::Bool bridge_msg;
  std_msgs::Empty hover_msg;

  void cmd2UAV_sub_callback(const test_msgs::floatlist::ConstPtr& msg);

  void status_sub_callback(const std_msgs::Bool::ConstPtr& msg);
    
  void UAVpos_sub_callback(
                  const geometry_msgs::PointStamped::ConstPtr& msg);
 };
}



#endif //UAV_CONTROL_CENTER_H

