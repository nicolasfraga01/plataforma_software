#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32


def callback(msg):
    print msg.data

rospy.init_node('subscriptor_simple')

sub=rospy.Subscriber('/contador',Int32,callback)
rospy.spin()