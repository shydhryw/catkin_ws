#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import roslib
roslib.load_manifest("agvs_sim_bringup")

from geometry_msgs.msg import Twist
from std_msgs.msg import String


class Teleop:
    def __init__(self):
        rospy.init_node("teleop_joy")

        pub = rospy.Publisher('cmd_vel', Twist)
        rospy.init_node('smartcar_teleop')
        rate = rospy.Rate(rospy.get_param('~hz', 1))
        self.cmd = None

        cmd = Twist()
        cmd.linear.x = 0.2
        cmd.linear.y = 0
        cmd.linear.z = 0
        cmd.angular.z = 0
        cmd.angular.z = 0
        cmd.angular.z = 0.5

        self.cmd = cmd
        while not rospy.is_shutdown():
            str = "hello world %s" % rospy.get_time()
            rospy.loginfo(str)
            pub.publish(self.cmd)
            rate.sleep()


if __name__ == "__main__":
    Teleop()