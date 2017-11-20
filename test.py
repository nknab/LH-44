# !/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep
from math import *
# from movement import *
# from parking import *
from line_following import *

# movement = Movement()
# parking = Parking()
line_following = LineFollowing()

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

# movement.move_rear_motors_forever(300)

# parking.parallel_park()

# line_following.calibrate_sensor()
# movement.steering(600, 0)
line_following.follow_line(0.5, 0, 0, 600, 1)

# print("Ev3")