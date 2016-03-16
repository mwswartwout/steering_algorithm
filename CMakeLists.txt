cmake_minimum_required(VERSION 2.8.3)
project(steering_algorithm)

find_package(catkin REQUIRED rospy)

catkin_python_setup()

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES steering_algorithm
#  CATKIN_DEPENDS other_catkin_pkg
#  DEPENDS system_lib
)

include_directories(${catkin_INCLUDE_DIRS})