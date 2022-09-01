# jmu_turtlebot3_bringup

Launch files that make working with TB3 in foxy a bit more convenient.

In part, these address the issue that the Turtlebot continues to obey
last `cmd_vel` message forever, which can be awkward if a control node
crashes or exits while the robot is moving.  the `safe_cmd_vel` node
periodically checks to see if no other nodes are publishing to
`cmd_vel` and if not, publishes a stop command.
