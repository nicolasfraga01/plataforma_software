#!/usr/bin/env python

import rospy
import numpy as np
from geometry_msgs.msg import Twist


rospy.init_node('simulacion_turtlrbot')
pub=rospy.Publisher('/mobile_base/commands/velocity',Twist,queue_size=1)

rate=rospy.Rate(2)
comando=Twist()
comando.linear.x=0.5
comando.linear.y=0.0
comando.linear.z=0.0
comando.angular.x=0.0
comando.angular.y=0.0
comando.angular.z=0.0

contador=0
print(contador)
while contador<5:
    contador=contador+1
    pub.publish(comando)
    rate.sleep()