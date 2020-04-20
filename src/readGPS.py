#!/usr/bin/env python
import rospy
from demining_19_20_rover_ros.msg import GPSint

class readGPS():
    update_rate = 1 #Hz
    def __init__(self):
        pub = rospy.Publisher('gps_data', GPSint, queue_size=5)
        rospy.init_node('readGPS', anonymous=True)

        rate = rospy.Rate(self.update_rate)
        while not rospy.is_shutdown():
            print("GPS")

            ## Get the GPS data and publish it using pub
            rate.sleep()

if __name__ == "__main__":
    obj = readGPS()
