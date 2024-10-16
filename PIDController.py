from machine import Pin
from utime import sleep
import machine

class PIDController:

    def __init__(self, kp:float, ki:float, kd:float, cycle_time_seconds:float, i_limit:float = 10.0) -> None:
        # settings
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.cycle_time_seconds = cycle_time_seconds
        self.i_limit = i_limit

        # state variables
        self.previous_error:float = 0.0
        self.previous_i:float = 0.0

    def calculate(self, actual:float, goal:float) -> float:
        error = goal - actual

        # P term
        P:float = error * self.kp

        # I term
        I:float = self.previous_i + (error * self.ki * self.cycle_time_seconds)
        I = max(min(I, self.i_limit), self.i_limit * -1)

        # D term
        D:float = self.kd * (error - self.previous_error) / self.cycle_time_seconds

        # set state variables for next time
        self.previous_error = error
        self.previous_i = I

        # return
        return P + I + D
    
    def reset(self) -> None:
        self.previous_error = 0.0
        self.previous_i = 0.0