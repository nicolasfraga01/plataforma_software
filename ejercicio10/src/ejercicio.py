#!/usr/bin/env python

import rospy

from sensor_msgs.msg import LaserScan


def callback(msg):
 
    distancia_izq=msg.ranges[len(msg.ranges)-1]
    distancia_der=msg.ranges[0]
    distancia_del=msg.ranges[len(msg.ranges)/2]
    vector=[distancia_izq,distancia_der,distancia_del]
    if min(vector)==distancia_izq:
        print "Distancia minima--> 180 grados(izquierda): ",distancia_izq
    elif min(vector)==distancia_der:
        print "Distancia minima--> 0 grados(derecha): ",distancia_der
    elif min(vector)==distancia_del:
        print "Distancia minima--> 90 grados(frontal): ", distancia_del


rospy.init_node('distmin_laser')
sub=rospy.Subscriber('/scan',LaserScan,callback)
rospy.Rate(10)
rospy.spin()
