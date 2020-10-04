#!/usr/bin/env python

import rospy

from sensor_msgs.msg import LaserScan


def callback(msg):
 
    distancia_izq=msg.ranges[719]
    distancia_der=msg.ranges[0]
    distancia_del=msg.ranges[360]
    vector=[distancia_izq,distancia_der,distancia_del]
    if min(vector)==distancia_izq:
        print "Distancia minima--> 180 grados: ",msg.ranges[719]
    elif min(vector)==distancia_der:
        print "Distancia minima--> 0 grados: ",msg.ranges[0]
    elif min(vector)==distancia_del:
        print "Distancia minima--> 90 grados: ", msg.ranges[360]
    


rospy.init_node('distmin_laser_11')
sub=rospy.Subscriber('/kobuki/laser/scan',LaserScan,callback)
rospy.Rate(10)
rospy.spin()