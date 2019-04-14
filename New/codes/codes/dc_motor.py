import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
 
Motor1A = 11
Motor1B = 13
#Motor1E = 15


GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
    #GPIO.setup(Motor1E,GPIO.OUT)
while True:     
    print ("Turning motor on")
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    #GPIO.output(Motor1E,GPIO.HIGH)
     
    time.sleep(2)
     
    print ("Stopping motor")
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    #GPIO.output(Motor1E,GPIO.HIGH)

    time.sleep(2)
     
    GPIO.cleanup()
