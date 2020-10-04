#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist



def callback(msg):
    mover=Twist()
    dist_del=msg.ranges[360]
    dist_der=msg.ranges[0]
    dist_izq=msg.ranges[179]

    if dist_del>1:    
        mover.linear.x=0.2
        pub.publish(mover)
        mover.linear.x=0
    elif dist_del<1:
        mover.angular.z=1
        pub.publish(mover)
        rate.sleep(2)
        mover.angular.z=0
    elif dist_der<1:
        mover.angular.z=1
        pub.publish(mover)
        rate.sleep(2)
        mover.angular.z=0
    elif dist_izq<1:
        mover.angular.z=-1
        pub.publish(mover)
        rate.sleep(2)
        mover.angular.z=0


rospy.init_node('sub_ej12')
pub=rospy.Publisher('/mobile_base/commands/velocity',Twist,queue_size=1)
sub=rospy.Subscriber('/scan',LaserScan,callback)
rate=rospy.Rate(10)
rospy.spin()
