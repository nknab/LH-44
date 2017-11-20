"""
@author nknab
@version 1.0
@date 15/11/2017
@description This is an emergency stop class for the LH44 that stops the robot when something is wrong.
"""

# !/usr/bin/env python3

from ev3dev.ev3 import *

"""
Declaring and Initializing the various motors
"""
front_motor = MediumMotor('outA')
right_motor = LargeMotor('outB')
left_motor = LargeMotor('outC')
# spare_motor = LargeMotor('outD')

"""
Stopping the various motors
"""
front_motor.stop(stop_action="brake")
left_motor.stop(stop_action="brake")
right_motor.stop(stop_action="brake")
# spare_motor.stop(stop_action="hold")
