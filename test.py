"""
@author nknab
@version 1.0
@date 15/11/2017
@description This is the main class of the LH44.
"""

# !/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep
from math import *

from parking import *
from movement import *

parking = Parking()
movement = Movement()

'''
movement.move_rear_motors_a_distance(300, 15)


movement.steering(300, -60)
movement.move_rear_motors_forever(-300)
sleep(1.5)
movement.stop_rear_motors()
# movement.stay_still(0)
'''
'''
movement.steering(300, 0)
sleep(15)
'''

# movement.move_rear_motors_forever(1000)

parking.parallel_park()

# line_following.calibrate_sensor()
# movement.steering(600, 0)
# line_following.follow_line(1, 0, 0, 1, 1)
