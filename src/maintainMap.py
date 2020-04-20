#!/usr/bin/env python
import rospy
from demining_19_20_rover_ros.msg import GPSint
from sensor_msgs.msg import LaserScan

class maintainMap():
    def __init__(self):
        rospy.init_node('maintainMap', anonymous='True')
        rospy.Subscriber("gps_data", GPSint, self.GPS_callback)
        rospy.Subscriber("lidar_data", LaserScan, self.lidar_callback)

        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            print("maintainMap")

            rate.sleep()
    
    def GPS_callback(self, data):
        pass

    def lidar_callback(self, data):
        pass

if __name__ == "__main__":
    obj = maintainMap()
