#!/usr/bin/env python3
#Author: Amrita

from ev3dev.ev3 import *
import ev3dev.ev3 as ev3

#define the touch sensor
ts = Touchsensor()

while True :
if ts.value()==1:
        Leds.set_color(Leds.LEFT,Leds.RED)
else :
        Leds.set_color(Leds.LEFT,Leds.GREEN)
