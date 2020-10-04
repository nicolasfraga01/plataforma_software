#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

global numero,contador,suma

numero=0
contador=0
suma=0

def callback(msg):
    global numero,suma,contador

    rospy.loginfo("Numero: %s",msg.data)

    numero=msg.data
    suma=suma+numero
    contador=contador+1

def sumador():
    global contador,suma,numero
    
    rospy.init_node('subscriptor_ejercicio8')
    sub=rospy.Subscriber('/mensaje_ejercicio6',Int32,callback)
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():

    	if contador<10:
            rate.sleep()
		    
        
        if contador==10:
            print "\nSuma-->{}\n".format(suma)
            contador=0
            suma=0

        rate.sleep()


if __name__ == "__main__":
    try:
        sumador()
    except rospy.ROSInterruptException:
        pass










