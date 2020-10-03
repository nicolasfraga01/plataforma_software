#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

rospy.init_node('publicador_ejercicio')
pub=rospy.Publisher('/mensaje_ejercicio6',Int32,queue_size=1)
rate=rospy.Rate(10)

numero=Int32()


while not rospy.is_shutdown(): 
    numero.data=int(input("Dame un numero: "))
    pub.publish(numero)
    rate.sleep()
