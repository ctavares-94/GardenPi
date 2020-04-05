#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [18]

# loop through pins and set mode and state to 'low'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations 18Hrs ON 

SleepTimeL = 300

# main loop

try:
  GPIO.output(18, GPIO.LOW)
  time.sleep(SleepTimeL); 
  GPIO.cleanup()

# End program cleanly with keyboard
except KeyboardInterrupt:

  # Reset GPIO settings
  GPIO.cleanup()#!/usr/bin/env python
