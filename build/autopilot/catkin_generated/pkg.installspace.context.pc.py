# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include".split(';') if "${prefix}/include" != "" else []
PROJECT_CATKIN_DEPENDS = "eigen_catkin;geometry_msgs;nav_msgs;position_controller;quadrotor_common;quadrotor_msgs;roscpp;state_predictor;std_msgs;trajectory_generation_helper".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lautopilot_helper".split(';') if "-lautopilot_helper" != "" else []
PROJECT_NAME = "autopilot"
PROJECT_SPACE_DIR = "/home/xslin/Documents/rpg_ws/install"
PROJECT_VERSION = "0.0.0"
