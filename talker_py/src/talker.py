#!/usr/bin/env python 

import rospy
from std_msgs.msg import Int32


rospy.init_node('publicador_simple')
pub=rospy.Publisher('/contador', Int32,queue_size=1)
rate=rospy.Rate(2)
contador=Int32()
contador.data=0
while not rospy.is_shutdown():
    pub.publish(contador)
    contador.data+=1
    rate.sleep()