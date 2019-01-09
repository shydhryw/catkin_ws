#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy 
import roslib
 
from sensor_msgs.msg import Joy
from std_msgs.msg import String, Float64
 
class Teleop:
    def __init__(self):
        roslib.load_manifest("agvs_sim_bringup")
        rospy.init_node("teleop_joy")
 
        self.turn_scale = 10.0
        self.drive_scale = 10.0
        self.deadman_button = 0.3
 
        self.cmd = None
        cmd_pub = rospy.Publisher("/agvs/joint_front_motor_wheel_controller/command", Float64, queue_size=10)
 
        # announce_pub = rospy.Publisher("/agvs/joint_front_motor_wheel_controller", String, latch=True)
        # announce_pub.publish(rospy.get_namespace())
 
        rospy.Subscriber("joy", Joy, self.callback)
        rate = rospy.Rate(rospy.get_param("~hz", 100))
 
        while not rospy.is_shutdown():
            rate.sleep()
            if self.cmd:
                cmd_pub.publish(self.cmd)
 
    def callback(self, data):
        """ Receive joystick data, formulate Twist message. """
        cmd = Float64
        cmd = data.axes[7] * self.turn_scale
        # cmd.linear.x = data.axes[1] * self.drive_scale
        # cmd.angular.z = data.axes[0] * self.turn_scale

        self.cmd = cmd
 
        # if data.buttons[self.deadman_button] == 1:
        #    self.cmd = cmd
        # else:
        #    self.cmd = None
 
if __name__ == "__main__":
    Teleop()