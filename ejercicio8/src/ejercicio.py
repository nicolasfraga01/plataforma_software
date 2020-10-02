#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32


def callback(msg):
    print msg.data

rospy.init_node('subscriptor_ejercicio8')
sub=rospy.Subscriber('/mensaje_ejercicio6',Int32,callback)

rospy.spin()