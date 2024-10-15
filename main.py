import MPU6050
from machine import Pin
from utime import sleep
import machine

"""creates an I2C object with the id of 0, with data on pin 12, and clock on pin 13"""
i2c = machine.I2C(0, sda=machine.Pin(12), scl=machine.Pin(13))

imu = MPU6050(i2c)

imu.wake()

"""Tuple type of (x, y, z)"""
gyro_data = imu.read_gyro_data()

pidpitch = PIDController()

pid_pitch = 
pid_roll =
pid_yaw =

t1:float = pid_pitch + pid_roll - pid_yaw
t2:float = pid_pitch - pid_roll + pid_yaw
t3:float = pid_roll + pid_yaw - pid_pitch
t4:float = 0 - pid_pitch - pid_roll - pid_yaw
