#! /usr/bin/env python

import rospy
import numpy
import math

d_gain = 1;
psi_gain = 1;
k = numpy.array([d_gain, psi_gain])


def calculate_error(psi_des, x, y, x0, y0):
    # The edge normal of our desired heading
    n = numpy.array([(-math.sin(psi_des)), (math.cos(psi_des))])
    d_x = x - x0  # Difference in x coordinate
    d_y = y - y0  # Difference in y coordinate
    d_err = numpy.array([d_x, d_y]).dot(n) # Lateral offset error of robot

    psi_actual = math.atan2(d_y, d_x)  # Actual heading of robot
    psi_err = psi_actual - psi_des

    return numpy.array([(d_err), (psi_err)]) # Return error vector


def get_omega(psi_des, x, y, x0, y0):
    error = calculate_error(psi_des, x, y, x0, y0) # Get current error vector
    return k.dot(error)
