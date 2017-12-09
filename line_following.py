"""
@author nknab
@version 1.0
@date 15/11/2017
@description This is the class that allows LH44 Follow the line.
"""

# !/usr/bin/env python3
from ev3dev.ev3 import *

from time import sleep
from movement import *
from feedback_control import *

movement = Movement()
feedback_control = FeedbackControl()

colour_sensor_1 = ColorSensor('in2')
touch_sensor = TouchSensor('in1')

colour_sensor_1.mode = 'COL-REFLECT'


class LineFollowing:
    """
    Declaring and Initializing the variables
    """
    m = 2.04
    x_1 = 59

    """
    This method gets the threshold values of the surface.
    """
    def calibrate_sensor(self):
        black_value = 0
        print("Place Color Sensor On Black And Press And Hold Touch Sensor")
        count = 0
        while count != 2:
            ts_val = touch_sensor.value()
            if count == 0 and ts_val == 1:
                black_value = int(round(colour_sensor_1.value(), 2))
                print(black_value)
                count += 1
                print("Place Color Sensor On White And Release Touch Sensor")
            elif count == 1 and ts_val == 0:
                white_value = int(round(colour_sensor_1.value(), 2))
                self.x_1 = white_value
                print(white_value)
                count += 1

                self.m = (100 - 0) / (white_value - black_value)
                # self.c = 100 - (self.m * white_value)

    """
    This method is calibrates the light sensor values.

    @:return y 
    """
    def calibrated_values(self, sensor_value):
        y = (self.m * sensor_value) - (self.m * self.x_1) + 100
        return y

    """
    This method is making sure values got are within bounds.

    @:parameter value, min_threshold, max_threshold
    @:return valid_value
    """
    @staticmethod
    def check(value, min_threshold, max_threshold):
        if value > max_threshold:
            valid_value = max_threshold
        elif value < min_threshold:
            valid_value = min_threshold
        else:
            valid_value = value

        return valid_value

    """
    This method is responsible for following the line.

    @:parameter kp, ki, kd, speed, side_of_line
    """
    def follow_line(self, kp, ki, kd, speed, side_of_line):
        target_value = 50
        integral = 0
        previous_error = 0
        offset = -15;

        self.calibrate_sensor()
        movement.move_rear_motors_forever(speed)

        count = 0
        while True:
            light_readings = round(colour_sensor_1.value(), 2)
            print("Raw Sensor Values: " + str(light_readings))
            value = self.calibrated_values(light_readings)
            print("Calibrated Values: " + str(value))
            error = target_value - value
            integral += error
            pid = round(feedback_control.pid_control(target_value, value, kp, ki, kd, previous_error, integral, offset), 2)
            previous_error = error
            angle = self.check((pid * side_of_line), -60, 60)
            print("Before Move Steering")
            movement.steering(angle)
            print("Angle: " + str(angle))
            print("Previous Error: " + str(previous_error))
            print(count)
            count += 1

