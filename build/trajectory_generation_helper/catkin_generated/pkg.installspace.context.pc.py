# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include".split(';') if "${prefix}/include" != "" else []
PROJECT_CATKIN_DEPENDS = "eigen_catkin;polynomial_trajectories;quadrotor_common;roscpp".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-ltrajectory_generation_helper".split(';') if "-ltrajectory_generation_helper" != "" else []
PROJECT_NAME = "trajectory_generation_helper"
PROJECT_SPACE_DIR = "/home/xslin/Documents/rpg_ws/install"
PROJECT_VERSION = "0.0.0"
