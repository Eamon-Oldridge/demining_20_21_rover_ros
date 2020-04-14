#!/usr/bin/env python
import rospy

def navigation():
	rospy.init_node('navigation', anonymous='True')

if __name__ == "__main__":
	navigation()
	print("YAY")

