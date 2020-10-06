#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist



def callback(msg):
    mover=Twist()
    distancia_izq=msg.ranges[len(msg.ranges)-1]
    distancia_der=msg.ranges[0]
    distancia_del=msg.ranges[len(msg.ranges)/2]
    
    if distancia_del>1:    
        mover.linear.x=0.5
        rospy.loginfo("Avanzando")
        pub.publish(mover)
        mover.linear.x=0
    elif distancia_del<1:
        mover.angular.z=1.5
        rospy.loginfo("Girando izq")
        pub.publish(mover)
        rate.sleep()
        mover.angular.z=0
    elif distancia_der<1:
        mover.angular.z=1.5
        rospy.loginfo("Girando izq")
        pub.publish(mover)
        rate.sleep()
        mover.angular.z=0
    elif distancia_izq<1:
        mover.angular.z=-1.5
        rospy.loginfo("Girando der")
        pub.publish(mover)
        rate.sleep()
        mover.angular.z=0


rospy.init_node('sub_ej12')
pub=rospy.Publisher('/mobile_base/commands/velocity',Twist,queue_size=1)
sub=rospy.Subscriber('/scan',LaserScan,callback)
rate=rospy.Rate(10)
rospy.spin()

