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
ev3= EV3Brick()

#initial a motor at port B
test_motor = Motor(Port.B)

ev3.speaker.beep()
wait(1000)
test_motor.run_target(500, 90)
ev3.speaker.beep(frequency=1000,duration=500)
test_motor.run_target(500, 90)
wait(1000)
ev3.speaker.beep(frequency=1000,duration=500)
test_motor.run_target(500, 90)
wait(1000)
ev3.speaker.beep(frequency=1000,duration=500)
test_motor.run_target(500, 90)
ev3.speaker.beep(frequency=1000,duration=500)
