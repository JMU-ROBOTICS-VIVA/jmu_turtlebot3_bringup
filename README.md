# jmu_turtlebot3_bringup
Package that addresses some rough edges with using TB3 with Dashing

Usage:

```
ros2 launch jmu_turtlebot3_bringup rviz2.launch.py
```


This will launch the `tb_fixer` node along with rviz2 with an
appropriate configuration file. The `tb_fixer` node fixes the
following issues:

- Scan messages don't show up in rviz because they run ahead of tf.
    - This node delays and republishes `/scan` messages on `/scan_viz`.
- Rviz expects `camera_info` messages on a different topic (When using Gazebo).
     - Republish `camera/camera_info` to `camera/image_raw/camera_info`
- Turtlebot continues to obey last `cmd_vel` message forever, which can
   be awkward if a control node crashes or exits while the robot is moving.
     - Periodically check to see if no other nodes are publishing to `cmd_vel`
       if not, publish a stop command.
