#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("Received message: %s", msg.data)


if __name__ == '__main__':
    rospy.init_node('sub_node', anonymous=True)
    rospy.Subscriber('/chat', String, callback)
    
    rospy.spin()
