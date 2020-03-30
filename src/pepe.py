#! /usr/bin/env python

import rospy  
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

targets = [[-3.00638651848,
            2.6760931015,
            -0.701847905216,
            0.712326833655],
            [3.09081745148,
            13.5923061371,
            0.999954059868,
            -0.00958530926594],
            [15.1371364594,
            2.67736124992,
            0.0045889776254,
            0.999989470587]
            ]

class Frog:
    def __init__(self):
        rospy.init_node("pepe")
        self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)

    def movebase_client(self, x, y, w, z):
        self.client.wait_for_server()
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = x
        goal.target_pose.pose.position.y = y
        goal.target_pose.pose.orientation.w = w
        goal.target_pose.pose.orientation.z = z

        self.client.send_goal(goal)
        wait = self.client.wait_for_result()
        if not wait:
            rospy.logerr("Action server not available!")
        else:
            return self.client.get_result()

if __name__ == "__main__":
    f = Frog()
    while not rospy.is_shutdown():
        for m in range(0,len(targets),1):
            x = targets[m][0]
            y = targets[m][1]
            w = targets[m][2]
            z = targets[m][3]
            status = f.movebase_client(x,y,w,z)
            print(status)
    
    
    
