#!/usr/bin/env python

import rospy

from sensor_msgs.msg import LaserScan


def callback(msg):
    '''
    print "Distancia 0 grados: ",msg.ranges[0]
    print "Distancia 90 grados: ", msg.ranges[359]
    print "Distancia 180 grados: ",msg.ranges[719]
    '''
    print "Distancia minima: ",msg.range_min


rospy.init_node('laser_turtlebot')
sub=rospy.Subscriber('/scan',LaserScan,callback)
rospy.Rate(2)
rospy.spin()
