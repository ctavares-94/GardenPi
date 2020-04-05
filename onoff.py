import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import time


# initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)        
relay = 18

# read data using pin 4
sensor = Adafruit_DHT.DHT22
pin = 4

# set temps
temp1 = 26.3
temp2 = 26.4

#pull data from sensor

while True:
    time.sleep(5)
    instance = Adafruit_DHT.read_retry(sensor, pin)

    Temp = instance[1]

    print (Temp)

                     
    if Temp <= temp1:
        GPIO.output(relay, GPIO.LOW) # on
        print("turning on relay")
                 
    if Temp >= temp2:
        GPIO.output(relay, GPIO.HIGH) # out
        print("turning off relay")


  # Reset GPIO settings
GPIO.cleanup()