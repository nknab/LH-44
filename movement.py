"""
@author nknab
@version 1.0
@date 15/11/2017
@description This is the movement class that controls the LH44.
"""

# !/usr/bin/env python3

from ev3dev.ev3 import *


class Movement:
    """
    Declaring and Initializing the various motors
    """
    front_motor = MediumMotor('outA')
    right_motor = LargeMotor('outB')
    left_motor = LargeMotor('outC')

    """
    This method is to check if the speed provided is beyond the thresholds.
    If it is, it reset it to the maximum and minimum values respectfully.
    
    @:parameter speed
    @:return spd
    """
    @staticmethod
    def speed_limit_check(speed):
        spd = speed
        if speed > 1000:
            spd = 1000
        elif speed < -1000:
            spd = -1000
        return spd

    """
    This method is for steering the LH44.
    
    @:parameter speed
    """
    def steering(self, speed=0):
        spd = self.speed_limit_check(speed)
        self.front_motor.run_forever(speed_sp=spd)

    """
    This method is for steering the LH44.

    @:parameter speed, angle
    """
    def steering_rel(self, speed=0, angle=0):
        spd = self.speed_limit_check(speed)
        self.front_motor.run_to_rel_pos(position_sp=angle, speed_sp=spd, stop_action="brake")
        self.front_motor.wait_while('running')

    """
    This method is for moving the LH44 forward or backward.

    @:parameter speed
    """
    def move_rear_motors_forever(self, speed=0):
        spd = self.speed_limit_check(speed)
        self.right_motor.run_forever(speed_sp=spd)
        self.left_motor.run_forever(speed_sp=spd)

    """
    This method is for moving the LH44 forward or backward a specific distance.

    @:parameter speed, distance
    """
    def move_rear_motors_a_distance(self, speed=0, distance=0):
        spd = self.speed_limit_check(speed)
        circumference = (2 * (22 / 7) * 1.86) * 3
        encoder_ticks = (360 * distance) / circumference
        self.right_motor.run_to_rel_pos(position_sp=encoder_ticks, speed_sp=spd, stop_action="brake")
        self.left_motor.run_to_rel_pos(position_sp=encoder_ticks, speed_sp=spd, stop_action="brake")
        self.right_motor.wait_while('running')
        self.left_motor.wait_while('running')

    """
    This method is for stopping the LH44.
    """
    def stop_rear_motors(self):
        self.left_motor.stop(stop_action="brake")
        self.right_motor.stop(stop_action="brake")
