"""

"""

import os
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node


def generate_launch_description():
    # We need to get the path to the .rviz file...
    this_prefix = get_package_share_directory('jmu_turtlebot3_bringup')
    rviz_path = os.path.join(this_prefix, 'rviz', 'model.rviz')

    return LaunchDescription([
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_dir, '--ros-args', '--remap', 'image_raw/camera_info:=camera_info'],
            output='screen'),
        Node(
            package='image_transport',
            executable='republish',
            name='republish',
            arguments=['compressed', 'in/compressed:=image_raw/compressed', 'raw', 'out:=image_raw/uncompressed'],
            output='screen'
            )
    ])
