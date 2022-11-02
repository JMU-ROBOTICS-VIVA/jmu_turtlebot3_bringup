#!/usr/bin/env python
"""Node to prevent the TB3 from following the last command forever.

By default, the TB3 continues to obey the most recently received Twist
message until another message arrives.  This makes it the
responsibility of controller nodes to send a stop message before
shutting down, which is inconvenient.

This node monitors the number of other publishers to /cmd_vel and
sends stop messages when it drops to 0.

Author: Nathan Sprague Version: 9/1/2022

"""
import rclpy
import rclpy.node

from geometry_msgs.msg import Twist


class SafeCmdNode(rclpy.node.Node):

    def __init__(self):
        super().__init__('safe_cmd_vel')
        self.thrust_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.create_timer(.1, self.timer_callback)

    def timer_callback(self):
        if self.count_publishers('cmd_vel') == 1:  # Just this node.
            twist = Twist()
            self.thrust_pub.publish(twist)


def main(args=None):
    rclpy.init(args=args)
    node = SafeCmdNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
