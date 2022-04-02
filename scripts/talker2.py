#!/usr/bin/env python
import rospy
from std_msgs.msg import String


def talker2():
    pub = rospy.Publisher('/world', String, queue_size=10)
    rospy.init_node('talker2', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        hello_str = "World!"
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker2()
    except rospy.ROSInterruptException:
        pass
