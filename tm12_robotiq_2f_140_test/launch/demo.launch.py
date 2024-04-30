import os
from launch import LaunchDescription
from launch_ros.actions import Node 
from launch.substitutions import Command, LaunchConfiguration
from moveit_configs_utils import MoveItConfigsBuilder
from launch_ros.parameter_descriptions import ParameterValue
from launch_param_builder import ParameterBuilder, load_yaml, load_xacro
import xacro

from ament_index_python import get_package_share_directory

from moveit_configs_utils.launch_utils import (
    add_debuggable_node,
    DeclareBooleanLaunchArg,
)
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
)

def generate_launch_description():

    ld = LaunchDescription()
    ld.add_action(DeclareBooleanLaunchArg("use_rviz", default_value=True))
    ld.add_action(DeclareLaunchArgument("publish_frequency", default_value="15.0"))
    model_launch_arg = DeclareLaunchArgument(
        name="model",
        default_value=os.path.join(
            get_package_share_directory("tm12_robotiq_2f_140_moveit_config"),
            "config/tm12.urdf.xacro"
        )
    )
    ld.add_action(model_launch_arg)

    moveit_config = MoveItConfigsBuilder("tm12", package_name="tm12_robotiq_2f_140_moveit_config").to_moveit_configs()
    
    robot_description = ParameterValue(
        Command(
            [
                'xacro ',
                LaunchConfiguration('model'),
            ]
        ),
        value_type=str
    )
    #robot_description = load_xacro(LaunchConfiguration('model')) 

    # broadcast static tf of virtual_joints
    ld.add_action(
        Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            name=f"static_transform_publisher",
            output="log",
            arguments=[
                "--frame-id",
                "world",
                "--child-frame-id",
                "base",
            ],
        )
    )
    # Given the published joint states, publish tf for the robot links
    rsp_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        respawn=True,
        output="screen",
        parameters=[
            moveit_config.robot_description, #robot_description, #
            {
                "publish_frequency": LaunchConfiguration("publish_frequency"),
            },
        ],
    )
    ld.add_action(rsp_node)

    return ld