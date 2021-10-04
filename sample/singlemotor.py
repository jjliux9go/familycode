#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch,DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Write your program here
#ev3= EV3Brick()

#initial a motor at port B
motor = Motor(Port.A)
irfsensor=InfrareSensor(Port.S4)

#ev3.speaker.beep()

Speed=0

def setSpeed(acc):
    global speed
    if acc < 0:
        speed = max(0, speed - 1)
    elif acc > 0:
        speed = min(3, speed + 1)
    else:
        speed = 0
    if speed > 0:
        motor.run(speed*90)
    else:
        motor.stop()

while True:
    if not any(brick.buttons()):
        wait(10)
    else:
        if Button.LEFT in brick.buttons():
            setSpeed(-1)
        elif Button.RIGHT in brick.buttons():
            setSpeed(1)
        elif Button.UP in brick.buttons():
            setSpeed(0)
        elif Button.CENTER in brick.buttons():
            setSpeed(0)
            break
        wait(1000)
if irfsersor.distance()< 200:
    setSpeed(0)
