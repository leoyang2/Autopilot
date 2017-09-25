#!/usr/bin/env python3
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

s = ev3.UltrasonicSensor('in1')

# Configure sensor mode
# 'US-DIST-CM' means that Continuous measurement in centimeters.

s.mode = 'US-DIST-CM'

# Create motor entity
# 'outA' is the port Medium motor is connected.

m = ev3.MediumMotor('outA')

# All the configurations are done so far
try:
	# Make a infinite loop
	while True:
		# Measure distance
		distance = s.value()
		# Because the speed range is from 0 - 1500
		# Here convert distance to speed
		# Suppose the valid distance range is from 5cm to 50cm
		if distance < 50:
			distance = 50
		if distance > 500:
			distance = 500

		# Call reMap function
		speed = reMap(distance, 500, 50, 1500, 0)
		# Start the motor to run at the given speed
		m.run_forever(speed_sp = speed)
		
		print('Current speed is %d'%speed)
		print('Current distance is %d'%distance)
#		time.sleep(1)

except KeyboardInterrupt:
	m.stop()
	
