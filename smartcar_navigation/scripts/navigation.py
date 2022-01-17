#!/usr/bin/env python

"""

    RoboCup@Home Education | oc@robocupathomeedu.org
    navi.py - enable turtlebot to navigate to predefined waypoint location

"""

import rospy

import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, PoseWithCovarianceStamped, Point, Quaternion, Twist
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from tf.transformations import quaternion_from_euler


start = 1

class NavToPoint:
    def __init__(self):
        rospy.on_shutdown(self.cleanup)
        
	# Subscribe to the move_base action server
        self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)

        rospy.loginfo("Waiting for move_base action server...")

        # Wait for the action server to become available
        self.move_base.wait_for_server(rospy.Duration(120))
        rospy.loginfo("Connected to move base server")
            
        rospy.loginfo("Ready to go")
	rospy.sleep(1)

	locations = dict()

	# Location A
	A_x = 2.93
	A_y = -1.43
	A_theta = 1.5708

	quaternionA = quaternion_from_euler(0.0, 0.0, A_theta)
	locations['A'] = Pose(Point(A_x, A_y, 0.000), Quaternion(quaternionA[0], quaternionA[1], quaternionA[2], quaternionA[3]))

        # Location B
	B_x = -1.18
	B_y = 2.63
	B_theta = 0
	quaternionB = quaternion_from_euler(0.0, 0.0, B_theta)
	locations['B'] = Pose(Point(B_x, B_y, 0.000), Quaternion(quaternionB[0], quaternionB[1], quaternionB[2], quaternionB[3]))

	# Location C
	C_x = -3.49
	C_y = -1.24
	C_theta = 0.12
	quaternionC = quaternion_from_euler(0.0, 0.0, C_theta)
	locations['C'] = Pose(Point(C_x, C_y, 0.000), Quaternion(quaternionC[0], quaternionC[1], quaternionC[2], quaternionC[3]))




	self.goal = MoveBaseGoal()
        rospy.loginfo("Starting navigation test")


	while not rospy.is_shutdown():
	    self.goal.target_pose.header.frame_id = 'map'
	    self.goal.target_pose.header.stamp = rospy.Time.now()

	    # Robot will go to point A
	    if start == 1:
		rospy.loginfo("Going to point A")
		rospy.sleep(2)
		self.goal.target_pose.pose = locations['A']
	  	self.move_base.send_goal(self.goal)
		waiting = self.move_base.wait_for_result(rospy.Duration(300))
		if waiting == 1:
		    rospy.loginfo("Reached point A")
		    rospy.sleep(2)
		    global start
		    start = 2

	    # After reached point A, robot will go back to initial position
	    elif start == 2:
		rospy.loginfo("Going to point B")
		rospy.sleep(2)
		self.goal.target_pose.pose = locations['B']
		self.move_base.send_goal(self.goal)
		waiting = self.move_base.wait_for_result(rospy.Duration(300))
		if waiting == 1:
		    rospy.loginfo("Reached point B")
		    rospy.sleep(2)
		    global start
		    start = 3
	    elif start == 3:
		rospy.loginfo("Going to point C")
		rospy.sleep(2)
		self.goal.target_pose.pose = locations['C']
		self.move_base.send_goal(self.goal)
		waiting = self.move_base.wait_for_result(rospy.Duration(300))
		if waiting == 1:
		    rospy.loginfo("Reached point C")
		    rospy.sleep(2)
		    global start
		    start = 0
            elif start == 0:
                cleanup()




    def cleanup(self):
        rospy.loginfo("Shutting down navigation	....")
	self.move_base.cancel_goal()

if __name__=="__main__":
    rospy.init_node('navi_point')
    try:
        NavToPoint()
        rospy.spin()
    except:
        pass

