
#!/usr/bin/env python 

# Todos
'''
Tutorial link: https://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29


1. Ensure the script is executed as python code

2. imports
Import 
- rospy 
- logging


3.intial the topic via publisher
4.intialize the node 
5. define the rate 


define the output string 
'''

import rospy
from std_msgs.msg import String


def talker():
    # publisher - (topic name, topic type, queue isze)
    t_pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.rate(10) #10hz

    while rospy.is_shutdown() == False:
        text_str = "hello world {0}".format(rospy.get_time())
        rospy.loginfo(text_str)
        t_pub.publish(text_str)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()

    except rospy.ROSInternalException:
        pass

