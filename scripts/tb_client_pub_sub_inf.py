#!/usr/bin/env python

import sys
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from rassignment.srv import *
from math import pi

pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=10)


def callback(data):
    global rad
    rad = int(data.data)
    print(rad)
    vel = tb_client(rad)
    print(vel)
    move = Twist()
    move.linear.x = 0.1
    move.angular.z = vel
    t = rospy.get_time()
    while not rospy.is_shutdown():
        tmp = rospy.get_time()
        if (tmp - t) > (2 * pi) / vel:
            move.angular.z = -move.angular.z
            t = rospy.get_time()
        print(move)
        rospy.loginfo(move)
        pub.publish(move)


def radius_sub():
    rospy.init_node("radius_sub", anonymous=True)
    rospy.Subscriber("/radius", String, callback)
    rospy.spin()


def tb_client(r):
    rospy.wait_for_service('compute_ang_vel')
    try:
        ang_vel = rospy.ServiceProxy('compute_ang_vel', compute_ang_vel)
        resp1 = ang_vel(int(r))
        return resp1.ang_vel
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)


if __name__ == "__main__":
    radius_sub()
