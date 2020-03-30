#Pepe Slam
#####ros navigation simulation
.dae files inside the world file have hardcoded path names. these need to set locally to run the navigation

###setup
1. follow marian tutorial on github (https://github.com/marckri/ROS-Helper/blob/master/doc/turtlebot3-sim.md)
2. create new package
3. copied default gazebo launchfile into package
4. download world files (https://github.com/hussamayoub/turtlebot3melodic.git)
5. added world files to package
6. edited simulation file with launch files
7. mapping file based on suii (https://github.com/RoboHubEindhoven/suii/tree/master/suii_bringup/launch)
8. navigation file based on suii
9. manual mapping using teleop_twist_joy
###coding and tweaking
10. nagivate and tweak with Rviz and rqt
11. use example python to set goal
12. create python script to loop between goals
### how to launch
rosboot in all terminals
new terminal launch SLAM_v1 turtleSim.launch
new terminal launch SLAM_v1 navigation.launch
new terminal rviz, 2d pos estimate
new terminal rosrun SLAM_v1 pepe.py