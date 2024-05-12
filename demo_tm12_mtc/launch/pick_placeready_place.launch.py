import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from moveit_configs_utils import MoveItConfigsBuilder


def generate_launch_description():
    moveit_config = (
        MoveItConfigsBuilder("tm12_robotiq_2f_140")
        .planning_pipelines(pipelines=["ompl"])
        .robot_description(file_path="config/tm12.urdf.xacro")
        .trajectory_execution(file_path="config/moveit_controllers.yaml")
        .to_moveit_configs()
    )

    pick_placeready_place = Node(
        package="demo_tm12_mtc",
        executable="pick_placeready_place",
        output="screen",
        parameters=[
            os.path.join(
                get_package_share_directory("demo_tm12_mtc"),
                "config",
                "tm12_config.yaml",
            ),
            moveit_config.robot_description,
            moveit_config.robot_description_semantic,
            moveit_config.robot_description_kinematics,
            moveit_config.planning_pipelines,
            moveit_config.joint_limits,
        ],
    )

    return LaunchDescription([pick_placeready_place])
