"""
@author nknab
@version 1.0
@date 15/11/2017
@description This is the parking class that controls the LH44.
"""

# !/usr/bin/env python3

from movement import *
from math import *

movement = Movement()
us = UltrasonicSensor()
us.mode = 'US-DIST-CM'


class Parking:

    l_1 = 41.0      # l_1 = Length of LH44
    w = 17.00       # w = width of LH44
    k = 6.30        # k = Distance from front wheel to the front of LH44
    l_2 = 31.20     # l_2 = The wheel base of LH44
    r = 55.70       # r = Radius of LH44's curb-to-curb turning circle

    def calculate_space_required(self):
        space = round((sqrt((pow(self.r, 2) - pow(self.l_2, 2)) + pow((self.l_2 + self.k), 2) - pow(
            (sqrt(pow(self.r, 2) - pow(self.l_2, 2)) - self.w), 2) - self.l_2 - self.k)), 2)
        # space = round(self.l_1 + (sqrt((pow(self.r, 2) - pow(self.l_2, 2)) + pow((self.l_2 + self.k), 2) - pow(
        #     (sqrt(pow(self.r, 2) - pow(self.l_2, 2)) - self.w), 2) - self.l_2 - self.k)), 2)
        return space

    def parallel_park(self):
        space = self.calculate_space_required() + 5
        movement.move_rear_motors_forever(300)
        while True:
            distance = us.value() / 10
            if distance > 15:
                movement.stop_rear_motors()
                print("Potential Parking Space")
                movement.move_rear_motors_a_distance(300, space)
                distance = us.value() / 10
                if distance > 10:
                    movement.steering(100, 60)
                    movement.move_rear_motors_a_distance(100, -17.6)
                    movement.steering(100, -60)
                    movement.move_rear_motors_a_distance(100, -8.8)
                    movement.steering(100, -60)
                    movement.move_rear_motors_a_distance(100, -17.6)
                    movement.steering(100, 60)
                    break
                else:
                    print("Insufficient Parking Space")
                    break



        '''
        while True:
            distance = us.value() / 10
            print(distance)
            if distance < 15:
                continue
            else:
                print("Potential Parking Space")
                movement.stop_rear_motors()
                movement.move_rear_motors_a_distance(300, space)
                distance = us.value() / 10
                if distance > 10:
                    movement.steering(100, 60)
                    movement.move_rear_motors_a_distance(100, 35.2)
                    movement.steering(100, -60)
                    movement.move_rear_motors_a_distance(-100, 17.6)
                    movement.steering(100, -60)
                    movement.move_rear_motors_a_distance(-100, 35.2)
                    movement.steering(100, 60)
                    break
                else:
                    print("Insufficient Parking Space")
                    break
        '''