import MPU6050
import PIDController
from machine import Pin
from utime import sleep
import machine

#creates an I2C object with the id of 0, with data on pin 12, and clock on pin 13
i2c = machine.I2C(0, sda=machine.Pin(12), scl=machine.Pin(13))

#creates the IMU object with the specified I2C
imu = MPU6050.MPU6050(i2c)

#turn on low pass filter to 5 (max 6)
imu.write_lpf_range(5)

imu.wake()

#change these values later
kp = 1
ki = 1
kd = 1

#create the PIDController object for pitch roll and yaw
pidpitch = PIDController.PIDController(kp, ki, kd, 0.004)
pidyaw = PIDController.PIDController(kp, ki, kd, 0.004)
pidroll = PIDController.PIDController(kp, ki, kd, 0.004)

while (True):
    #tuple of (x, y, z) gyroscope data
    gyro_data = imu.read_gyro_data()

    #calculate the desired pitch roll and yaw using gyroscope data
    pid_pitch = pidpitch.calculate(gyro_data[0], 0)
    pid_yaw = pidyaw.calculate(gyro_data[1], 0)
    pid_roll = pidroll.calculate(gyro_data[2], 0)

    #instructions for all four motors
    t1:float = pid_pitch + pid_roll - pid_yaw
    t2:float = pid_pitch - pid_roll + pid_yaw
    t3:float = pid_roll + pid_yaw - pid_pitch
    t4:float = 0 - pid_pitch - pid_roll - pid_yaw

    #test to see if code is working
    print(t1, t2, t3, t4)