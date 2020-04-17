#!/usr/bin/env python
import rospy
from demining_19_20_rover_ros.msg import GPSint
update_rate = 1 #Hz

def readGPS():
    pub = rospy.Publisher('gps_data', GPSint, queue_size=5)
    rospy.init_node('readGPS', anonymous=True)

    rate = rospy.Rate(update_rate)
    while not rospy.is_shutdown():
        print("GPS")

        ## Get the GPS data and publish it using pub
        rate.sleep()

if __name__ == "__main__":
    readGPS()
