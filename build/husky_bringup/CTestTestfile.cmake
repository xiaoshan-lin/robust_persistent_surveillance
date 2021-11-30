# CMake generated Testfile for 
# Source directory: /home/xslin/Documents/xslin/research/rpg_ws/src/husky/husky_bringup
# Build directory: /home/xslin/Documents/xslin/research/rpg_ws/build/husky_bringup
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_husky_bringup_roslaunch-check_launch "/home/xslin/Documents/xslin/research/rpg_ws/build/husky_bringup/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/xslin/Documents/xslin/research/rpg_ws/build/husky_bringup/test_results/husky_bringup/roslaunch-check_launch.xml" "--return-code" "/usr/bin/cmake -E make_directory /home/xslin/Documents/xslin/research/rpg_ws/build/husky_bringup/test_results/husky_bringup" "/opt/ros/melodic/share/roslaunch/cmake/../scripts/roslaunch-check -o \"/home/xslin/Documents/xslin/research/rpg_ws/build/husky_bringup/test_results/husky_bringup/roslaunch-check_launch.xml\" \"/home/xslin/Documents/xslin/research/rpg_ws/src/husky/husky_bringup/launch\" ")
subdirs("gtest")
