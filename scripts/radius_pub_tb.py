#!/usr/bin/env python
import rospy
from std_msgs.msg import String


def radius_pub():
    pub = rospy.Publisher('/radius', String, queue_size=10)
    rospy.init_node('radius_pub', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        radius_str = "1"
        rospy.loginfo(radius_str)
        pub.publish(radius_str)
        rate.sleep()


if __name__ == '__main__':
    try:
        radius_pub()
    except rospy.ROSInterruptException:
        pass
