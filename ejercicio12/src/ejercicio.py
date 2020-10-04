#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


def callback(msg):
    distancia_izq=msg.ranges[719]
    distancia_der=msg.ranges[0]
    distancia_del=msg.ranges[360]
    mover=Twist()
    if distancia_del>1:
        mover.linear.x=0.5
        pub.publish(mover)
    elif distancia_del<1:
        mover.angular.z=-90
        pub.publish(mover)
    elif distancia_der<1:
        mover.angular.z=-90
        pub.publish(mover)
    elif distancia_izq<1:
        mover.angular.z=90
        pub.publish(mover)
    
rospy.init_node('sub_ej12')
sub=rospy.Subscriber('/kobuki/laser/scan',LaserScan,callback)
pub=rospy.Publisher('/mobile_base/commands/velocity',Twist,queue_size=1)
rospy.Rate(2)
rospy.spin()