#!/usr/bin/env python3
from ev3dev.ev3 import *
import ev3dev.ev3 as ev3

ev3.Sound.speak('Welcome Group 5! If you can hear me that is a good thing').wait()
time.sleep(3)
ev3.Sound.speak('How are you?').wait()
time.sleep(3)
