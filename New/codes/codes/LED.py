import RPi.GPIO as GPIO               #import gpio libraries
import time                           #import time


GPIO.setmode(GPIO.BOARD) 	      #set GPIO as per board
GPIO.setup(11,GPIO.OUT)               #set 11th pin as output
#GPIO.setup(13,GPIO.OUT)

while 1:                              #infinite loop
  GPIO.output(11,GPIO.HIGH)           #set 11th pin high
  #GPIO.output(13,GPIO.HIGH)           #set 13th pin high
  time.sleep(1)                      #suspends execution for 1sec
  GPIO.output(11,GPIO.LOW)            #set 11th pin low
  #GPIO.output(13,GPIO.LOW)	      #set 11th pin low
  time.sleep(1)                      

