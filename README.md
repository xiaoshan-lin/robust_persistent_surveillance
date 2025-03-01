# Robust Planning for Persistent Surveillance with Energy-Constrained UAVs and Mobile Charging Stations
## Table of contents
- [Quick start](#quick-start)
-  [Notice](#notice)
- [Status](#status)
- [What's included](#whats-included)
- [Bugs and feature requests](#bugs-and-feature-requests)
- [Contributing](#contributing)
- [Creators](#creators)
- [Thanks](#thanks)
- [Copyright and license](#copyright-and-license)
## Quick start
This code is run and tested on Ubuntu 18.04 with ROS melodic and python3.
For installation instructions of ROS, check out http://wiki.ros.org/Distributions 

Open a terminal, 
```
cd your_preferred_directory
mkdir YOUR_WS
cd YOUR_WS
git clone https://github.com/xiaoshan-lin/robust_persistent_surveillance.git src
sudo apt update
sudo apt install ros-melodic-lms1xx ros-melodic-move-base ros-melodic-twist-mux ros-melodic-rviz-imu-plugin
catkin build
echo "source /path/to/YOUR_WS/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
 ```
1. run the off-line planner
```
cd YOUR_WS/src/robust_persistent_surveillance/test/scripts/persistent_surveillance 
python3 test.py
```
> **Note**  In test.py, edit prm in the test() function. Parameters that you need to specify: r - number of UAVs; m - dimension of the environment in the y axis; n - dimension of the environment in the x axis; h - height of the UAVs when monitoring; v_max - maximum velocity of the UAVs; u_max - maximum velocity of the UGVs; footprint - sensor detection footprint; beta: - energy depletion rate; e - maximum energy of the UAVs  when fully charged; robust - robustness degree; solver - TSP solver (options: "concorde", "lkh", "christofides"); planner - planning scheme (options: "max", "exhaustive").
> **Note** You will need to install some python modules to sucessfully run the code. Use pip3 to install needed modules (e.g. in terminal run``pip3 install elkai``to install elkai module) 

> **Note** test.py will compute the off-liner plans for UAVs and UGVs with the given parameters. The results will be saved in YOUR_WS/src/robust_persistent_surveillance/test/resource for use in gazebo simulation.
2. Run Gazebo simulation
To run the gazebo simulation, run
``roslaunch rps_planning sim.launch
``
> **Note** This will launch one UGV teams with 4 UAVs in the gazebo simulation. If you want to add more UGV teams, open YOUR_WS/src/robust_persistent_surveillance/test/launch/sim.launch and uncomment the code block under the comment "launch 2nd UAV-UGV team". If you want to modify the number of UAVs for each team, open test/launch/spawn_UAV_UGV_team.launch and you will see several groups like <group ns="$(arg mav_name)$(arg uav0)">, <group ns="$(arg mav_name)$(arg uav1)">; each group is used for spawning one UAV. For example, to reduce the number of UAVs to 3, simply removing the following code block would work.
```
<group ns="$(arg mav_name)$(arg uav3)">
    <include file="$(find rotors_gazebo)/launch/spawn_mav.launch">
      <arg name="mav_name" value="$(arg mav_name)" />
     ... 
    <node name="uav_control_center" pkg="test" type="uav_control_center" output="screen" 
          args="$(find test)/resource 3 0 2">  
       <remap from="cmd2UAV" to="/$(arg robot_namespace)/cmd2UAV"/>
    </node> 
 </group> 
```
<!-- 
> **Note** To increase the number of UAVs for each team (which I don't recommend since the code is not well written for that), a lot more modification will be needed. For example, initial position of the UAVs will need to be redesigned, see arg x and arg y in spawn_UAV_UGV_team.launch; more UAV group in spawn_UAV_UGV_team.launch will be needed; more UAV global index(uav0,uav1, ...) in sim.launch will be needed; in test/scripts/husky_control_center.py, more UAV topics and callback functions will be needed.

> **Note**  Currently the UGV motion planner doesn't work well, especially for turtlebot. I would recommend using husky (by setting UGV_name = 0 in sim.launch)

## Notice
The code is not yet completed. Improvement will be made in the future (including adding LICENSE and acknowledgement)  before publishing. Please do not share the code.
-->




