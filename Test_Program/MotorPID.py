#!/usr/bin/env python3
#Author: Coor

from ev3dev.ev3 import *
import ev3dev.ev3 as ev3

# This is the function I made for remapping values. 
# You can just skip this function and look it later.
def reMap(value, maxInput, minInput, maxOutput, minOutput):

	value = maxInput if value > maxInput else value
	value = minInput if value < minInput else value

	inputSpan = maxInput - minInput
	outputSpan = maxOutput - minOutput

	scaledThrust = float(value - minInput) / float(inputSpan)

	return minOutput + (scaledThrust * outputSpan)

# Create ultrasonic sensor entity, 
# 'in1' is the port sensor is connected.

s = ev3.ColorSensor('in2')

# Configure sensor mode
# 'US-DIST-CM' means that Continuous measurement in centimeters.

s.mode = 'COL-REFLECT'

# Create motor entity
# 'outA' is the port Medium motor is connected.

m1 = ev3.MediumMotor('outD')
m2 = ev3.LargeMotor('outA')
m3 = ev3.LargeMotor('outB')

KP = 1
KI = 1
KD = 0

Black = 9
White = 70
middle = (White - Black)/2 + Black
lasterror = 0
integral = 0

speed = -200
# All the configurations are done so far
try:
	# Make a infinite loop
	while True:
		# Measure distance
		value = s.value()
		# Because the speed range is from 0 - 1500
		# Here convert distance to speed
		# Suppose the valid distance range is from 5cm to 50cm
		
		error = middle - value
		integral = error + integral
		derivative = error - lasterror
		
		correction = KP * error + KI * integral + KD * derivative
		
		lasterror = error
		# Call reMap function
		#position = reMap(corr, KP*(color-), 50, 1500, 0)
		# Start the motor to run at the given speed
		#m.run_forever(speed_sp = speed)
		if correction >30:
			correction = 30
		elif correction <-30 :
			correction = -30
			
		print('Current color is %d'%value)
		print('Current corr is %d'%correction)
		m1.run_to_abs_pos(speed_sp = 1000, position_sp = correction, stop_action = "hold")
		m2.run_forever(speed_sp = speed)
		m3.run_forever(speed_sp = speed)
#		time.sleep(1)

except KeyboardInterrupt:
	m1.stop(stop_action = "brake")
	m2.stop()
	m3.stop()
