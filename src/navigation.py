#!/usr/bin/env python
import rospy

class navigation():
	def __init__(self):
		rospy.init_node('navigation', anonymous='True')

if __name__ == "__main__":
	obj = navigation()
