import RPi.GPIO as GPIO
import time
count=0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)

while True:

        i=GPIO.input(11)
        if i==0:
                print "not detected",i
                time.sleep(1)
        elif i==1:
		print "detected",i
                time.sleep(0)
	

