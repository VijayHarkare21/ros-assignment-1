#!/usr/bin/env python

from __future__ import print_function

from rassignment.srv import trajectory, trajectoryResponse
import rospy


def handle_trajectory(req):
    t = 0
    inter_x = []
    inter_y = []
    while(t < 10):
        print("Returning [%s + %s * %s, %s + %s * %s]" %
              (req.x, req.vx, t, req.y, req.vy, t))
        resp1 = trajectoryResponse()
        inter_x.append(req.x + req.vx * t)
        inter_y.append(req.y + req.vy * t)
        t = t + 1
    resp1.xi = inter_x
    print(inter_x)
    resp1.yi = inter_y
    print(inter_y)
    return resp1.xi, resp1.yi


def trajectory_server():
    rospy.init_node('trajectory_server')
    s = rospy.Service('trajectory', trajectory, handle_trajectory)
    print("Ready to give intermediate trajectory")
    rospy.spin()


if __name__ == '__main__':
    trajectory_server()
