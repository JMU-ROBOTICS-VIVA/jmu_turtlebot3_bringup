import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

import rclpy
import rclpy.node

def get_node_names():
    """Return all active node names."""
    rclpy.init()
    node = rclpy.create_node('__anonymous')
    rclpy.spin_once(node, timeout_sec=.2)
    names = node.get_node_names()
    node.destroy_node()
    return names

def generate_launch_description():
    tb3_dir = get_package_share_directory('turtlebot3_bringup')
    tb3_launch_file_dir = os.path.join(tb3_dir, 'launch')

    ld = LaunchDescription()

    node_names = get_node_names()

    if 'safe_cmd_vel' not in node_names:
        ld.add_entity(Node(
            package="jmu_turtlebot3_bringup",
            executable="safe_cmd_vel",
            name="safe_cmd_vel",
            output="screen",
        ))

    ld.add_entity(IncludeLaunchDescription(
        PythonLaunchDescriptionSource([tb3_launch_file_dir,
                                       '/rviz2.launch.py']),
    ))

    return ld
