#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry


def callback(msg):
    print "Posicion:\n{}".format(msg.pose.pose.position)

rospy.init_node('pos_turtlebot')
sub=rospy.Subscriber('/odom',Odometry,callback)
rospy.Rate(2)
rospy.spin()
