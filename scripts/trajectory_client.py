#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from rassignment.srv import *
import numpy as np

from matplotlib import pyplot as pp


def trajectory_client(x, y, vx, vy):
    rospy.wait_for_service('trajectory')
    try:
        traj = rospy.ServiceProxy('trajectory', trajectory)
        resp1 = traj(x, y, vx, vy)
        return resp1.xi, resp1.yi
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)


def usage():
    return "%s [x y vx vy]" % sys.argv[0]


if __name__ == "__main__":
    if len(sys.argv) == 5:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        vx = int(sys.argv[3])
        vy = int(sys.argv[4])
    else:
        print(usage())
        sys.exit(1)
    pp.plot(list(trajectory_client(x, y, vx, vy)[0]), list(
        trajectory_client(x, y, vx, vy)[1]))
    pp.tight_layout()
    pp.show()
