# Omron TM12 with robotiq 2F 140 gripper MoveIt 2

This project is demonstrates a setup of Omron TM12 cobot with a Robotiq 2F 140 gripper for simulation and *control using the planning capabilities of [MoveIt 2](https://moveit.ros.org/). 

The project also uses [MoveIt Task Constructor Framework](https://github.com/moveit/moveit_task_constructor.git) to simulate a simple pick and place task.


The main branch is configured for [ROS2 Humble Hawksbill](https://docs.ros.org/en/humble/Installation.html).

## Setup
1. Create workspace and clone the repository

```
mkdir -p tm12_tmr/src
cd tm12_tmr/src 

git clone https://github.com/MasterpieceNKA/tm12_tmr.git
``` 

2. Download dependencies

```
for repo in tm12_tmr/tm12_2f140.repos; do vcs import < "$repo"; done

rosdep update

rosdep install -r --from-paths . --ignore-src --rosdistro $ROS_DISTRO -y
```

3. Build workspace

```
cd .. 

colcon build --mixin release --executor sequential
```
## Running MoveIt 2 demo
 
Open new terminal and run

```
source install/setup.bash  && ros2 launch demo_tm12_moveit demo.launch.py
```  

[![YouTube: Omron TM12 with Robotiq 2F 140 gripper MoveIt 2](https://img.youtube.com/vi/yElqukeEtx8/0.jpg)](https://www.youtube.com/watch?v=yElqukeEtx8 "YouTube: Omron TM12 with Robotiq 2F 140 gripper MoveIt 2")

## Running MoveIt Task demo
 
Open new terminal and run

```
source install/setup.bash  && ros2 launch demo_tm12_mtc demo.launch.py
```

Open second terminal or terminal tab and run
```
source install/setup.bash  && ros2 launch demo_tm12_mtc pick_placeready_place.launch.py
```

[![YouTube: Omron TM12 with Robotiq 2F 140 gripper MoveIt Task Planner](https://img.youtube.com/vi/pyy533-DBvI/0.jpg)](https://www.youtube.com/watch?v=pyy533-DBvI "YouTube: Omron TM12 with Robotiq 2F 140 gripper MoveIt Task Planner") 

## Future directions
1. Create config file that uses DH parameters downloaded from an Omron TM12 cobot to update nominal URDF robot model
2. Test code using actual Omron TM12 cobot
3. Incorporate Hand-Eye calibration to use cobot's camera
