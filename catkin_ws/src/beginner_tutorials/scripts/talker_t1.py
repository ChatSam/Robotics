#!/usr/bin/env python 

import rospy
from std_msgs.msg import String


def talker():
    # publisher - (topic name, topic type, queue isze)
    t_pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) #10hz

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

