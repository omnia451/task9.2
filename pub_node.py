#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    
    rospy.init_node('pub_node', anonymous=True)
    pub = rospy.Publisher('/chat', String, queue_size=10)
    
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        hello_str = "hello from publisher"
        pub.publish(hello_str)
        
        rate.sleep()
    
