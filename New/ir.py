import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)

while True:

    i=GPIO.input(11)
    if i==0:
        print "detected"
        time.sleep(0.1)
    else:
        print "not detected"
        time.sleep(0.1)
    
