/*
 * Copyright 2015 Fadri Furrer, ASL, ETH Zurich, Switzerland
 * Copyright 2015 Michael Burri, ASL, ETH Zurich, Switzerland
 * Copyright 2015 Mina Kamel, ASL, ETH Zurich, Switzerland
 * Copyright 2015 Janosch Nikolic, ASL, ETH Zurich, Switzerland
 * Copyright 2015 Markus Achtelik, ASL, ETH Zurich, Switzerland
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0

 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include <uav_control_center.h>
#include <sstream>
#include <math.h>

namespace rotors_gazebo{

UAV_CONTROL_CENTER::UAV_CONTROL_CENTER(
const ros::NodeHandle& nh, const ros::NodeHandle& private_nh)
    :nh_(nh),
    private_nh_(private_nh){
        
    trajectory_pub =
      nh_.advertise<quadrotor_msgs::Trajectory>("autopilot/trajectory", 10);

    bridge_pub =
      nh_.advertise<std_msgs::Bool>("bridge/arm", 10);  
  
    hover_pub =
      nh_.advertise<std_msgs::Empty>("autopilot/force_hover", 10);  
     
    cmd2UGV_pub = nh_.advertise<std_msgs::Bool>(
      "cmd2UGV", 10);

     turnoffmotor_pub = 
          nh_.advertise<std_msgs::Empty>("autopilot/off", 10);

     status_sub = nh_.subscribe("autopilot/status",10,
                    &UAV_CONTROL_CENTER::status_sub_callback,this);

     cmd2UAV_sub = nh_.subscribe("cmd2UAV",10,
                    &UAV_CONTROL_CENTER::cmd2UAV_sub_callback,this);

     UAVpos_sub = nh_.subscribe("ground_truth/position",10,
                    &UAV_CONTROL_CENTER::UAVpos_sub_callback, this);

    is_stop = false;
   
    empty_point.velocity.linear = tf2::toMsg(
                            tf2::Vector3(0.0, 0.0, 0.0));
    empty_point.velocity.angular = tf2::toMsg(
                            tf2::Vector3(0.0, 0.0, 0.0));
    empty_point.acceleration.linear = tf2::toMsg(
                            tf2::Vector3(0.0, 0.0, 0.0));
    empty_point.acceleration.angular = tf2::toMsg(
                            tf2::Vector3(0.0, 0.0, 0.0));
    empty_point.jerk.linear = tf2::toMsg(
                            tf2::Vector3(0.0, 0.0, 0.0));
    empty_point.jerk.angular = tf2::toMsg(
                            tf2::Vector3(0.0, 0.0, 0.0));
    empty_point.snap.linear = tf2::toMsg(
                            tf2::Vector3(0.0, 0.0, 0.0));
    empty_point.snap.angular = tf2::toMsg(
                            tf2::Vector3(0.0, 0.0, 0.0));
    empty_point.heading = 0.0;
    empty_point.heading_rate = 0.0;
    empty_point.heading_acceleration = 0.0;
     
    bridge_msg.data = true;


    }
UAV_CONTROL_CENTER::~UAV_CONTROL_CENTER() {}
                

int UAV_CONTROL_CENTER::uav_trajectory_publisher(std::vector<waypointstruct>&new_waypoints, double disp_x, double disp_y){
        ROS_INFO("Started trajectory_publisher.");

        trajectory_point = empty_point;
        double k_t;
        size_t next_idx;
        double time_begin = 0.1;
        quadrotor_msgs::Trajectory trajectory;
       
        for (size_t i = 0; i < new_waypoints.size()-1; ++i) {

            //std::cout << "read" << i << "point\n";
            waypointstruct& wp = new_waypoints[i];
            if (i==new_waypoints.size()-1){
                next_idx = 0;
            }else{
                next_idx = i+1;
            }
                       
            waypointstruct& wp_next = new_waypoints[i+1]; 
            x = wp.x + disp_x;
            y = wp.y + disp_y;
            z = wp.z;
            std::cout<<"this pos:("<<x<<","<<y<<","<<z<<")\n";
            yaw = wp.yaw;
            x_next = wp_next.x + disp_x;
            y_next = wp_next.y + disp_y;
            z_next = wp_next.z;
            //std::cout<<"next pos:("<<x_next<<","<<y_next<<","<<z_next<<")\n";

            yaw_next = wp_next.yaw;

            if (i==0){
                last_x = x;
                last_y = y;
                last_z = pt.z;
            }

            dist2next = sqrt(pow(x - x_next , 2) + pow(y - y_next , 2) + pow(z - z_next , 2));
            t2next = dist2next/ave_vel;
            if (t2next < 0.8){
                t2next = 1.0;
            }
            std::cout<<"time segment = "<<t2next<<std::endl;
 
            a_x = -1*(6*(x - x_next))/pow(t2next, 5);
            b_x = (15*(x - x_next))/pow(t2next, 4);
            c_x = -1*(10*(x - x_next))/pow(t2next, 3);
            d_x = x;

            a_y = -1*(6*(y - y_next))/pow(t2next, 5);
            b_y = (15*(y - y_next))/pow(t2next, 4);
            c_y = -1*(10*(y - y_next))/pow(t2next, 3);
            d_y = y;

            a_z = -1*(6*(z - z_next))/pow(t2next, 5);
            b_z = (15*(z - z_next))/pow(t2next, 4);
            c_z = -1*(10*(z - z_next))/pow(t2next, 3);
            d_z = z;

            for (size_t k = 0; k < 50; ++k) {
               
               k_t = k*t2next/50;
               pose.position.x = a_x * pow(k_t, 5) + b_x * pow(k_t, 4) + 
                                 c_x * pow(k_t, 3) + d_x;
               pose.position.y = a_y * pow(k_t, 5) + b_y * pow(k_t, 4) + 
                                 c_y * pow(k_t, 3) + d_y;
               pose.position.z = a_z * pow(k_t, 5) + b_z * pow(k_t, 4) + 
                                 c_z * pow(k_t, 3) + d_z;

               myQuaternion.setRPY(0,0,yaw);
               orientation = tf2::toMsg(myQuaternion);
               pose.orientation = orientation;
               trajectory_point.pose = pose;

               trajectory_point.velocity.linear = tf2::toMsg(tf2::Vector3(
               5* a_x * pow(k_t, 4) + 4 * b_x * pow(k_t, 3) + 3 * c_x * pow(k_t, 2), 
               5* a_y * pow(k_t, 4) + 4 * b_y * pow(k_t, 3) + 3 * c_y * pow(k_t, 2), 
               5* a_z * pow(k_t, 4) + 4 * b_z * pow(k_t, 3) + 3 * c_z * pow(k_t, 2)
               ));
               trajectory_point.acceleration.linear = tf2::toMsg(tf2::Vector3(
                    20 * a_x * pow(k_t, 3) + 12 * b_x * pow(k_t, 2) + 6 * c_x * k_t, 
                    20 * a_y * pow(k_t, 3) + 12 * b_y * pow(k_t, 2) + 6 * c_y * k_t,
                    20 * a_z * pow(k_t, 3) + 12 * b_z * pow(k_t, 2) + 6 * c_z * k_t
               ));
               trajectory_point.jerk.linear = tf2::toMsg(tf2::Vector3(
                    60 * a_x * pow(k_t, 2) + 24 * b_x * k_t + 6 * c_x, 
                    60 * a_y * pow(k_t, 2) + 24 * b_y * k_t + 6 * c_y, 
                    60 * a_z * pow(k_t, 2) + 24 * b_z * k_t + 6 * c_z
               ));
               trajectory_point.snap.linear = tf2::toMsg(
                       tf2::Vector3(120 * a_x * k_t + 24 * b_x, 
                                    120 * a_y * k_t + 24 * b_y, 
                                    120 * a_z * k_t + 24 * b_z ));
                     
               trajectory_point.time_from_start = ros::Duration(k_t+time_begin);
               trajectory.points.push_back(trajectory_point);
               
            }
            time_begin = time_begin + t2next;
            
        }   
  
            trajectory.type = trajectory.GENERAL; 
            trajectory.header.stamp = ros::Time::now();

            while (trajectory_pub.getNumSubscribers() == 0 && ros::ok()) {
              ros::Duration(0.5).sleep();
              ROS_INFO("GET STUCK");
            }
            ros::Duration(2.0).sleep();
            trajectory_pub.publish(trajectory);
            
            return 1;

}

void UAV_CONTROL_CENTER::bridge_publisher(){
     while (bridge_pub.getNumSubscribers() == 0 && ros::ok()) {
              ros::Duration(0.5).sleep();
              ROS_INFO("Waitting for subscriber of bridge publisher");
        }
     ROS_INFO("[%s] Connectting Bridge",
                private_nh_.getNamespace().c_str());    
     bridge_pub.publish(bridge_msg);
}

void UAV_CONTROL_CENTER::hover_publisher(){
     ROS_INFO("[%s] Hover",
                private_nh_.getNamespace().c_str());
     hover_pub.publish(hover_msg);
}

void UAV_CONTROL_CENTER::cmd2UAV_sub_callback(const rps_msgs::floatlist::ConstPtr& msg){
    flight_info.type = msg -> type;
    flight_info.x = msg -> x;
    flight_info.y = msg -> y;
    flight_info.heading_idx = msg -> idx;
    ROS_INFO("--UAV get msgs from the UGV--");
    
}

void UAV_CONTROL_CENTER::status_sub_callback(const std_msgs::Bool::ConstPtr& msg){
    is_stop = msg->data;
    ROS_INFO("----get turn off msg----");
}

void UAV_CONTROL_CENTER::UAVpos_sub_callback(
        const geometry_msgs::PointStamped::ConstPtr& msg){
    pt = msg->point;
}
}

int main(int argc, char** argv) {
  
  
  int idx;
  int new_idx;
 
  ros::init(argc, argv, "uav_control_center");
  ROS_INFO("*******************************************");
  ROS_INFO("uav_control_center launched successfully");
  ros::NodeHandle nh;
  ros::NodeHandle private_nh("~");
  rotors_gazebo::UAV_CONTROL_CENTER uav_control_center(nh, private_nh);
  nh.getParam("/UAV/average_velocity", uav_control_center.ave_vel);
  nh.getParam("/UAV/controller_sample_rate", uav_control_center.sample_rate);
  ros::V_string args;
  std::vector<std::vector<waypointstruct>> waypoints[4];
  ROS_INFO("***********************");
  std::vector<waypointstruct> new_waypoints;
  std::vector<waypointstruct>::iterator vtr_begin;
  std_msgs::Empty motormsg; 
  std_msgs::Bool UGVmsg;
  ros::removeROSArgs(argc, argv, args);
  ROS_INFO("******");
  idx = std::stoi(args.at(2));
  double wait_time;
  wait_time = std::stoi(args.at(3));
  double height;
  height = std::stod(args.at(4));
  
  
  int NumOfUav = 4;
  
  geometry_msgs::Point pt;
  geometry_msgs::Point c_pt;
  double hover_yaw_1;
  double hover_yaw_2;
  int stage = 0;  
  //print_flag
  int p_tf = 0;
  double x_1, y_1, z_1, yaw_1;
  double disp_x, disp_y; 
  int result;
  ros::Rate rate(10);
  std::string error_msg;
  
  for (int p = 0; p < 4; p++){
    for (int i = 0; i < NumOfUav; i++) {
        std::vector<waypointstruct> waypoints_;
        std::ifstream wp_file(args.at(1)+"/waypoint_"+std::to_string(p)+"_"
                        +std::to_string(i)+".txt");

        if (wp_file.is_open()) {

        // Only read complete waypoints.
          while (wp_file >> x_1 >> y_1 >> z_1 >> yaw_1) {
            waypoints_.push_back(waypointstruct(x_1, y_1, z_1, yaw_1));
           }
           wp_file.close(); 
           ROS_INFO("Read %d waypoints.", (int)waypoints_.size());
           waypoints[p].push_back(waypoints_);
           } else {
           error_msg = args.at(1)+"/waypoint_"+std::to_string(p)+"_"
                        +std::to_string(i)+".txt";
           ROS_ERROR_STREAM("Unable to open poses file: " << error_msg);
           return -1;
          }
    }
  }

  uav_control_center.bridge_publisher();

  while (ros::ok()){
    
    if (stage == 0){     
      if (uav_control_center.flight_info.type < 4){
        if (p_tf == 0){
            ROS_INFO("UAV in stage 0");
            p_tf = p_tf + 1;
        }     
        ROS_INFO("Ready to fly");
    
        new_idx = idx + uav_control_center.flight_info.heading_idx;
        new_idx = (int)remainder(new_idx,NumOfUav);
        if (new_idx < 0){
            new_idx = new_idx + NumOfUav;
        }
        new_waypoints = waypoints[uav_control_center.flight_info.type][new_idx]; 

        if (new_waypoints.size()>0){
            uav_control_center.hover_publisher();
            
            disp_x = uav_control_center.flight_info.x;
            disp_y = uav_control_center.flight_info.y;
            //add the hover point and landing point to the trajectory
              
            c_pt = uav_control_center.pt;
            std::cout<<"(x,y,z)=("<<c_pt.x<<","<<c_pt.y<<","<<c_pt.z<<")"<<std::endl;
            vtr_begin =  new_waypoints.begin();
            hover_yaw_1 = new_waypoints[0].yaw;
            hover_yaw_2 = new_waypoints[new_waypoints.size()-1].yaw;
        
            vtr_begin =  new_waypoints.insert (vtr_begin, 
                waypointstruct(c_pt.x - disp_x,c_pt.y - disp_y, height, hover_yaw_1));

            vtr_begin =  new_waypoints.insert (vtr_begin, 
                waypointstruct(c_pt.x-disp_x,c_pt.y-disp_y,c_pt.z, hover_yaw_1));

            new_waypoints.push_back(
                waypointstruct(c_pt.x-disp_x,c_pt.y-disp_y, height, hover_yaw_2));

            new_waypoints.push_back(
                    waypointstruct(c_pt.x-disp_x,c_pt.y-disp_y,c_pt.z, hover_yaw_2));
            stage = 1;  
        }else{
            stage = 2;
        }
     }
      
    }else if (stage == 1){
        if (p_tf == 1){
            ROS_INFO("UAV in stage 1");
            p_tf = p_tf + 1;
        }
        ros::Duration(wait_time).sleep();
        result = uav_control_center.uav_trajectory_publisher(new_waypoints, disp_x, disp_y); 
        stage = 2;


     }else if (stage == 2){
        if (p_tf == 2){
            ROS_INFO("UAV in stage 2");
            p_tf = 0;
        }

        //UAV finish all monitoring
        //Turn off the motors
        while (!uav_control_center.is_stop){
            ros::Duration(0.1).sleep();
            ros::spinOnce();
            continue;
        }
        uav_control_center.is_stop = false;
        uav_control_center.turnoffmotor_pub.publish(motormsg);
        ROS_INFO("Turning off UAV motors");

        UGVmsg.data = true;
        ros::Duration(1).sleep();
        uav_control_center.cmd2UGV_pub.publish(UGVmsg);
        ROS_INFO("Publishing landing msg to UGV");
        uav_control_center.flight_info.type = 4;

        stage = 0;     
        }
   
    ros::spinOnce();
    rate.sleep();
  }

  return 0;

}
