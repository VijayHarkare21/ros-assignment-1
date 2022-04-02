#!/usr/bin/env python
import rospy
from std_msgs.msg import String

pub = rospy.Publisher("/helloworld", String, queue_size=10)
world = "some_string"


def callback0(data):
    global world
    world = data.data


def callback1(data):
    rospy.Subscriber("/world", String, callback0)
    s = data.data + " " + world
    rospy.loginfo(s)
    pub.publish(s)


def pub_sub():
    rospy.init_node("pubsub", anonymous=True)
    rospy.Subscriber("/hello", String, callback1)
    rospy.spin()


if __name__ == '__main__':
    pub_sub()
