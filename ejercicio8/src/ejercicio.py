#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

global numero
numero=0
contador=0
suma=0

def callback(msg):
    global numero
    rospy.loginfo("Numero: %s",msg.data)
    numero=msg.data

def sumador():
    global contador, suma,contador
    rospy.init_node('subscriptor_ejercicio8')
    sub=rospy.Subscriber('/mensaje_ejercicio6',Int32,callback)
    rate=rospy.Rate(2)
    while contador!=11:
        
        suma+=int(numero)
        contador+=1
        rate.sleep()
        
    
    print "Suma-->{}".format(suma)


sumador()










