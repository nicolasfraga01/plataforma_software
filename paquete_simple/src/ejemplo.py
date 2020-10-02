#!/usr/bin/env python 
import rospy

rospy.init_node("nodo_basico")
rate=rospy.Rate(2)
while not rospy.is_shutdown():
    print("mensaje de prueba")
    rate.sleep()