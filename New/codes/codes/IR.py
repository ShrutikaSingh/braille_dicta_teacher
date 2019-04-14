import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)         #disable all warnings
GPIO.setmode(GPIO.BOARD)        #set pin as per board
GPIO.setup(11, GPIO.IN)         #Read output from IR motion sensor
GPIO.setup(13, GPIO.OUT)        #output for LED
'''
GPIO.setup(13, GPIO.IN)         #Read output from IR motion sensor
GPIO.setup(15, GPIO.IN)         #Read output from IR motion sensor
#GPIO.setup(3, GPIO.OUT)         #LED output pin
'''
while True:

       i=GPIO.input(11)
       if i==0:                    #When output from IR sensor is LOW
             print "key1 Detected"
             GPIO.output(13, 1)    #Turn ON LED
             time.sleep(0.5)
             
       else:
              print "not detected"
              GPIO.output(13, 0)   #Turn OFF LED
              time.sleep(0.5) 
