#!/usr/bin/python 

from __future__ import print_function

from beginner_tutorials.srv import AddTwoInts, AddTwoIntsResponse

import rospy

def handle_add_two_ints(req):
    num1 = req.a
    num2 = req.b
    print("Returning values for [%s + %s = %s]" % (num1, num2, num1+num2))
    return AddTwoIntsResponse(num1+num2)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    # AddTwoInts is the service type
    serv = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print("ready to add two ints")
    rospy.spin()


if __name__ == "__main__":
    add_two_ints_server()