cmake_minimum_required(VERSION 2.8.3)
project(steering_algorithm)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
    roscpp
    tf
    std_msgs
    nav_msgs
    geometry_msgs
    cwru_srv
    mobot_pub_des_state
)

## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)


## Uncomment this if the package has a setup.py. This macro ensures
## modules and global scripts declared therein get installed
## See http://ros.org/doc/api/catkin/html/user_guide/setup_dot_py.html
# catkin_python_setup()

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES amcl_steering
#  CATKIN_DEPENDS rospy
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
# include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
)

## Declare a C++ library
# add_library(amcl_steering
#   src/${PROJECT_NAME}/amcl_steering.cpp
# )

## Add cmake target dependencies of the library
## as an example, code may need to be generated before libraries
## either from message generation or dynamic reconfigure
# add_dependencies(amcl_steering ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## Declare a C++ executable
add_executable(linear_steering_wrt_odom src/linear_steering_wrt_odom.cpp)
add_executable(pub_des_state_path_client_escape src/pub_des_state_path_client_escape.cpp)

## Add cmake target dependencies of the executable
## same as for the library above
# add_dependencies(amcl_steering_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## Specify libraries to link a library or executable target against
target_link_libraries(linear_steering_wrt_odom
   ${catkin_LIBRARIES}
)

target_link_libraries(pub_des_state_path_client_escape ${catkin_LIBRARIES})