import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)         #set GPIO as per board(R-Pi)
GPIO.setup(11,GPIO.OUT)          #set 11th pin as output pin

while True:                      #infinite
 GPIO.output(11,GPIO.HIGH)       #light gets turn on
 time.sleep(3)                   #turn on for 3 sec
 GPIO.output(11,GPIO.LOW)        #light gets off
 time.sleep(3)


