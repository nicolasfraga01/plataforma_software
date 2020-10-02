#!/usr/bin/env python

import rospy
import math
from sensor_msgs.msg import LaserScan


def callback(msg):
    print min(msg.range[360])

rospy.init_node('laser_turtlebot')
sub=rospy.Subscriber('/scan',LaserScan,callback)
rospy.Rate(2)
rospy.spin()
