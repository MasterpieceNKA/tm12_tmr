# tm12_tmr
TM12 with robotiq 2F 140 gripper

git clone https://github.com/MasterpieceNKA/tm12_tmr.git
for repo in tm12_tmr/tm12_2f140.repos; do vcs import < "$repo"; done
rosdep install -r --from-paths . --ignore-src --rosdistro $ROS_DISTRO -y


colcon build --mixin release --parallel-workers 3
