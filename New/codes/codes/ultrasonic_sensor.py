import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


TRIG = 11               #11th pin to TRIG
ECHO = 13               #13th pin to ECHO

print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)    #11th pin set as o/p
GPIO.setup(ECHO,GPIO.IN)      #13th pin set as i/p
GPIO.setwarnings(False)
GPIO.output(TRIG, False)     #TRIG set to low    
print "Waiting For Sensor To Settle"
time.sleep(2)


while True:
 GPIO.output(TRIG, True)        #triggering sensor
 time.sleep(0.00001)
 GPIO.output(TRIG, False)       #triggering sensor

 while GPIO.input(ECHO)==0:     #checking for echo pin
   pulse_start = time.time()                 

 while GPIO.input(ECHO)==1:     #checking for echo pin
   pulse_end = time.time()

 pulse_duration = pulse_end - pulse_start    #calculate  echoing time
 #distance =       time     * velo
 
 distance = pulse_duration * 17150           

 distance = round(distance, 2) #rounded to two decimal digits
 #distance/=2
 print "Distance:",distance,"cm"
 time.sleep(0.5)

#GPIO.cleanup()
