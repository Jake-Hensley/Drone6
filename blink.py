from machine import Pin
from utime import sleep
import machine

i2c = machine.I2C(0, sda=machine.Pin(12), scl=machine.Pin(13))

imu = MPU6050(i2c)

imu.wake()

gyro_data = imu.read_gyro_data()

print(gyro_data)