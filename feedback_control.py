"""
@author nknab
@version 1.0
@date 15/11/2017
@description This is a Feedback Control.
"""


class FeedbackControl:
    """
    This method is calculates the error.
    
    @:parameter target_value, value
    @:return error 
    """
    @staticmethod
    def calculate_error(target_value, value):
        error = target_value - value
        return error

    """
    This method is P controller.
    
    @:parameter target_value, value, kp
    @:return p
    """
    def p_control(self, target_value, value, kp):
        error = self.calculate_error(target_value, value)
        p = error * kp
        return p

    """This method is PD controller.
    
    @:parameter target_value, value, kp, kd, previous_error
    @:return pd
    """
    def pd_control(self, target_value, value, kp, kd, previous_error):
        p = self.p_control(target_value, value, kp)
        error = self.calculate_error(target_value, value)
        derivative = error - previous_error
        d = derivative * kd
        pd = p + d
        return pd

    """
    This method is PID controller.
    
    @:parameter target_value, value, kp, ki, kd, previous_error, integral
    @:return pid
    """
    def pid_control(self, target_value, value, kp, ki, kd, previous_error, integral, offset):
        pd = self.pd_control(target_value, value, kp, kd, previous_error)
        i = integral * ki
        pid = pd + i
        if pid > 0:
            pid += abs(offset)
        elif pid == 0:
            pid += abs(offset)
        elif pid < 0:
            pid += offset
        return pid