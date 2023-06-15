#ifndef WAYPOINTSTRUCT_H
#define WAYPOINTSTRUCT_H

#include<ros/ros.h>
#include <Eigen/Core>

class waypointstruct {
    public:
      waypointstruct(double _x, double _y, double _z, double _yaw)
              : x(_x), y(_y), z(_z), yaw(_yaw) {
    }
      double x;
      double y;
      double z;
      double yaw;
 };

#endif



