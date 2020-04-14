#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

update_rate = 1 #Hz

def readLidar():
    pub = rospy.Publisher('lidar_data', LaserScan, queue_size=5)
    rospy.init_node('readLidar', anonymous=True)

    rate = rospy.Rate(update_rate)
    while not rospy.is_shutdown():
        print("lidar")

        ## Get the lidar data and publish it using pub
        rate.sleep()

if __name__ == "__main__":
    readLidar()
