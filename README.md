# tm12_tmr
TM12 with robotiq 2F 140 gripper


mkdir -p tm12_tmr_mtc_demo/src

cd tm12_tmr_mtc_demo/src 

git clone https://github.com/MasterpieceNKA/tm12_tmr.git

for repo in tm12_tmr/tm12_2f140.repos; do vcs import < "$repo"; done

rosdep install -r --from-paths . --ignore-src --rosdistro $ROS_DISTRO -y

# change directory into tm12_tmr_mtc_demo workspace
cd .. 

colcon build --mixin release --parallel-workers 3

# terminal 1
source install/setup.bash  && ros2 launch demo_tm12_mtc demo.launch.py

# terminal 2
source install/setup.bash  && ros2 launch demo_tm12_mtc pick_placeready_place.launch.py



