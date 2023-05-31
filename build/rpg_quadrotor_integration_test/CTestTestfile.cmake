# CMake generated Testfile for 
# Source directory: /home/xslin/Documents/rpg_ws/src/rpg_quadrotor_control/test/rpg_quadrotor_integration_test
# Build directory: /home/xslin/Documents/rpg_ws/build/rpg_quadrotor_integration_test
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_rpg_quadrotor_integration_test_rostest_launch_rpg_quadrotor_integration_test.launch "/home/xslin/Documents/rpg_ws/build/rpg_quadrotor_integration_test/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/xslin/Documents/rpg_ws/build/rpg_quadrotor_integration_test/test_results/rpg_quadrotor_integration_test/rostest-launch_rpg_quadrotor_integration_test.xml" "--return-code" "/usr/bin/python2 /opt/ros/melodic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/xslin/Documents/rpg_ws/src/rpg_quadrotor_control/test/rpg_quadrotor_integration_test --package=rpg_quadrotor_integration_test --results-filename launch_rpg_quadrotor_integration_test.xml --results-base-dir \"/home/xslin/Documents/rpg_ws/build/rpg_quadrotor_integration_test/test_results\" /home/xslin/Documents/rpg_ws/src/rpg_quadrotor_control/test/rpg_quadrotor_integration_test/launch/rpg_quadrotor_integration_test.launch ")
subdirs("gtest")
