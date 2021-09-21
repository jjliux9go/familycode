#!/usr/bin/env python3

from time import sleep
import os
import sys

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

ts = TouchSensor()
leds = Leds()
#m = LargeMotor(OUTPUT_A)
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
sound = Sound()

#m.on_for_rotations(SpeedPercent(75), 5)
# drive in a turn for 5 rotations of the outer motor
# the first two parameters can be unit classes or percentages.
tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(75), 10)

# drive in a different turn for 3 seconds
tank_drive.on_for_seconds(SpeedPercent(60), SpeedPercent(30), 3)
sleep(3)

sound.speak('Welcome to the E V 3 dev project!')
sleep(3)

def set_font(name):
    '''Sets the console font

    A full list of fonts can be found with `ls /usr/share/consolefonts`
    '''
    os.system('setfont ' + name)

def main():
    '''The main function of our program'''

    set_font('Lat15-Terminus24x12')

    print("Press the touch sensor to change the LED color!")

    while True:
        if ts.is_pressed:
            leds.set_color("LEFT", "GREEN")
            leds.set_color("RIGHT", "GREEN")
        else:
            leds.set_color("LEFT", "RED")
            leds.set_color("RIGHT", "RED")
        # don't let this loop use 100% CPU
        sleep(0.01)

if __name__ == '__main__':
    main()
