#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
#ev3= EV3Brick()

#initial a motor at port B
motor = Motor(Port.A)
#irfsensor=InfrareSensor(Port.S4)

#ev3.speaker.beep()

SPEED = 100
STEERING = 90

STATUS_STOPPED = 0
STATUS_FORWARD = 1
STATUS_BACKWARD = 2
STATUS_STEERING = 3

COLORS = (None, Color.GREEN, Color.RED, Color.YELLOW)

"""
class Driver():
    def __init__(self, leftMotor, rightMotor, diameter, axle):
        self.driver = DriveBase(leftMotor, rightMotor, diameter, axle)
        slef.x = 0
        self.y = 0
        self.speed = 0
        self.steering = 0

    def drive(self, speed, steering):
        self.speed = speed
        self.steering = steering
        if self.speed == 0:
            self.driver.stop()
        else:
            self.driver.drive(self.speed, self.steering)
"""

class Robot():
    def __init__(self,leftMotor, rightMotor, topMotor, diameter, axle, maxSpeed=300, maxSteering=180, port=Port.S4):
        self.driver = Driver(leftMotor, rightMotor, diameter, axle)
        #self.cannon = topMotor
        #self.ultrasonic = UltrasonicSensor(port)
        self.speedStep = 32767 // maxSpeed
        self.steeringStep = 32767 // maxSteering
        self.active = True

    def drive(self, x, y):
        # map y (-32768 ~ +32767) to speed (-maxSpeed ~ +maxSpeed):
        speed = -y // self.speedStep
        # map x (-32768 ~ 32767) to steering (-maxSteering ~ +maxSteering):
        steering = x // self.steeringStep
        self.driver.drive(speed, steering)

"""
    def target(self, x):
        self.cannon.run(-x // 327)

    def fire(self):
        brick.sound.file('cannon.wav')

    def inactive(self):
        self.active = False
        self.drive(0, 0)
        brick.sound.beep()
"""

def main():
    brick.sound.beep()
wait(10000)
Main()
