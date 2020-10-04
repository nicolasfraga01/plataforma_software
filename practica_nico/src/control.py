#!/usr/bin/env python

#required modules
import rospy
import numpy as np
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

range_ahead=10
sensor_derecha=0.0
sensor_izquierda=0.0

def scan_callback(msg): #funcion que se invoca cada vez que se recibe un mensaje dentro del topic
    global range_ahead 
    
    #float32 angle_min  , start angle of the scan [rad]
    #float32 angle_max   , end angle of the scan [rad]
    # with zero angle being forward along the x axis
   
    #Podemos ver las caracteristicas de barrido.... INFO QUE SE PUBLICA POR EL TOPIC
    #rospy.loginfo("angle min %f",msg.angle_min) #angulo minimo en el que empieza el barrido
    #rospy.loginfo("angle max %f",msg.angle_max) #angulo maximo en el que acaba el barrido
    #rospy.loginfo("angle_increment %f",msg.angle_increment)  # angular distance between measurements [rad] 
                                                              #cada cuanto hago una lectura del escaner laser
   
    anglemin=np.rad2deg(msg.angle_min)
    anglemax=np.rad2deg(msg.angle_max)
    angleincrement=np.rad2deg(msg.angle_increment)
    #rospy.loginfo ("deg min %f",anglemin) #muestro por pantalla los angulos
    #rospy.loginfo ("deg max %f",anglemax)
    #rospy.loginfo("deg increment %f",angleincrement)

    #Podemos ver los valores devueltos por el escaner laser
    #for i in range (0,len(msg.ranges),1):
    #    currentangle=anglemin+i*angleincrement
    #    rospy.loginfo ("i %d current angle %f distance %f",i,currentangle,msg.ranges[i])
    global sensor_derecha
    global sensor_izquierda

    sensor_derecha=msg.ranges[0] 
    sensor_izquierda=msg.ranges[359] 
    #coge haz laser hacia la mitad del array...
    range_ahead=msg.ranges[len(msg.ranges)/2]  
    #rospy.loginfo(range_ahead)

def scan_and_move():
    rospy.init_node ('movedor_robot')
    pub=rospy.Publisher('/cmd_vel',Twist,queue_size=1)
    scan_sub=rospy.Subscriber('/kobuki/laser/scan',LaserScan,scan_callback) #topic ; tipo mensaje ; funcion scan_callback
    rate=rospy.Rate(4) #frecuencia de trabajo
    move=Twist()
    #print ("distancia delante ",range_ahead)

    while not rospy.is_shutdown():
       
        print ("distancia delante ",range_ahead)

        if range_ahead<0.2:
            move.linear.x=-3.25
            move.angular.z=0
    

        elif range_ahead<1.25: 

            if sensor_izquierda<sensor_derecha: 
                move.linear.x=0.5
                move.angular.z=-1.5

            elif sensor_izquierda>sensor_derecha:
                move.linear.x=0.5 
                move.angular.z=1.5 

        else:             
            move.linear.x=1.25
            move.angular.z=0.0  
            
        pub.publish(move)

        rate.sleep() #fuerza parada para trabajar a 4 Hz

if __name__ == '__main__':
   
    try:
        scan_and_move()
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated. ")