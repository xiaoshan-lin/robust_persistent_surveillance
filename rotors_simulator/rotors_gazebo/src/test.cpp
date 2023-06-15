#include <fstream>
#include <ros/ros.h>
#include <std_msgs/Bool.h>
#include <waypointstruct.h>

int main(int argc, char** argv) {

  std::vector<waypointstruct> waypoints[5];

  int NumOfUav = 1;
  
  double x_1, y_1, z_1, yaw_1;
  
  for (int i = 0; i < NumOfUav; i++) {
  std::ifstream wp_file("/home/xslin/Documents/xslin/research/rpg_ws/src/test/resource/waypoint_"+std::to_string(i)+".txt");

  if (wp_file.is_open()) {

// Only read complete waypoints.
  while (wp_file >> x_1 >> y_1 >> z_1 >> yaw_1) {
    waypoints[i].push_back(waypointstruct(x_1, y_1, z_1, yaw_1));
   }
   wp_file.close(); 
      } else {
     return -1;
  }
  }

  std::cout << waypoints[0].size();

}


