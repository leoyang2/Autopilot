#!/usr/bin/env python3
#Author: Amrita

from ev3dev.ev3 import *
import ev3dev.ev3 as ev3

#ev3.Sound.speak('Welcome Group 5! Today we are going to talk about test environment').wait()
#time.sleep(3)
#ev3.Sound.speak('ahhhhhhhhhhhhh time is passing so fast').wait()
#time.sleep(3)

# Create ultrasonic sensor entity,
# 'in1' is the port sensor is connected.

s = ev3.ColorSensor('in2')
s.mode = 'COL-COLOR'

# Configure sensor mode
# 'US-DIST-CM' means that Continuous measurement in centimeters.


# Create motor entity
# 'outA' is the port Medium motor is connected.

m = ev3.MediumMotor('outB')

KP = 1
KI = 1
KD = 0

Black = 4
White = 80
Mid = (White - Black)/2 + Black



# All the configurations are done so far
try:
	# Make a infinite loop
	while True:
		# Measure distance
		color = s.value()
		# Because the speed range is from 0 - 1500
		# Here convert distance to speed
		# Suppose the valid distance range is from 5cm to 50cm
		corr = KP * (Mid - color)

		# Call reMap function
		#position = reMap(corr, KP*(color-), 50, 1500, 0)
		# Start the motor to run at the given speed
		#m.run_forever(speed_sp = speed)

		#print('Current speed is %d'%speed)
		#print('Current distance is %d'%distance)
		m.run_to_abs_pos(speed_sp = 1000, position_sp = corr, stop_action = "hold")
#		time.sleep(1)

except KeyboardInterrupt:
	m.stop()
