#!/usr/bin/env python

from __future__ import print_function
from rassignment.srv import compute_ang_vel, compute_ang_velResponse
import rospy

linear_vel = 0.1


def handle_angular_velocity(req):
    print("Returning [%s / %s]" % (linear_vel, req.r))
    resp1 = compute_ang_velResponse()
    resp1.ang_vel = linear_vel / req.r
    print(resp1.ang_vel)
    return resp1.ang_vel


def tb_server():
    rospy.init_node('tb_angular_velocity', anonymous=True)
    s = rospy.Service('compute_ang_vel', compute_ang_vel,
                      handle_angular_velocity)
    print("Ready to calculate angular velocity")
    rospy.spin()


if __name__ == "__main__":
    tb_server()
