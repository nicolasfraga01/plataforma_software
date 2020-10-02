#!/usr/bin/env python
# license removed for brevity

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty
from sensor_msgs.msg import LaserScan #esto habra que sustituirlo por rplidar...

g_range_ahead=10
range_ahead=10

def scan_callback(msg):
  global g_range_ahead
  global range_ahead
  g_range_ahead=min(msg.ranges)
  range_ahead=msg.ranges(len(msg.ranges)/2)  
  rospy.loginfo("hola ???????????????????????????????????????????")
  rospy.loginfo (range_ahead)

def move(speed,distance,is_forward): #distance es la distancia umbral!!!
  velocity_message=Twist()
  
  if (is_forward):
    velocity_message.linear.x=abs(speed)
  else:
    velocity_message.linear.x=-abs(speed)

  scan_sub=rospy.Subscriber('scan',LaserScan,scan_callback)

  distance_moved=0.0
  loop_rate=rospy.Rate(10)#we publish the velocity at 10Hz
  velocity_publisher=rospy.Publisher('/cmd_vel_mux/input/teleop',Twist,queue_size=1000)
  t0=rospy.Time.now().to_sec()
  time.sleep(1.0)
  t0=rospy.Time.now().to_sec()
  while True:
    
    rospy.loginfo("turtlesim moves....")
    velocity_publisher.publish(velocity_message)
    loop_rate.sleep()
    t1=rospy.Time.now().to_sec()

    distance_moved=(t1-t0)*speed
    rospy.loginfo ("t1 %d t0 %d distance_moved %f", t1,t0,distance_moved)
    if (g_range_ahead<distance):
      rospy.loginfo("distance reached")
      break
  
  #we stop the robot
  velocity_message.linear.x=0
  velocity_publisher.publish(velocity_message)

def rotate(angular_speed_degree,relative_angle_degree,clockwise):
  #by default in ROS all angles are in radians, for angles and angular velocities

  velocity_message = Twist()
  velocity_message.linear.x=0
  velocity_message.linear.y=0
  velocity_message.linear.z=0
  velocity_message.angular.x=0
  velocity_message.angular.y=0
  velocity_message.angular.z=0

  
  angular_speed=math.radians(abs(angular_speed_degree))
  if (clockwise):
    velocity_message.angular.z=-abs(angular_speed)
  else:
    velocity_message.angular.z=abs(angular_speed)

  angle_moved=0.0
  loop_rate=rospy.Rate(10)
  velocity_publisher=rospy.Publisher('/cmd_vel_mux/input/teleop',Twist,queue_size=1000)

  t0=rospy.Time.now().to_sec()

  while True:
    rospy.loginfo("turtlesim rotates....")
    velocity_publisher.publish(velocity_message)
    
    t1=rospy.Time.now().to_sec()
    angle_degree_moved=(t1-t0)*angular_speed_degree
    loop_rate.sleep()

    if (angle_degree_moved>relative_angle_degree):
      rospy.loginfo("angle reached ")
      break

  #finally, stop the robot
  velocity_message.angular.z=0
  velocity_publisher.publish(velocity_message)
    
    
if __name__ == '__main__':
	
    try:
		  #publisher()
      rospy.init_node('turtlesim_roberto',anonymous=True)
      rotate(30,90,False)
      move(0.3,0.5,True)
      time.sleep(1.0)
     

    except rospy.ROSInterruptException:
        rospy.loginfo ("node terminated. ")
