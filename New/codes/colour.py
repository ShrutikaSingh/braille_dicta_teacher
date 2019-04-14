import RPi.GPIO as GPIO
import time
import serial


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

S0=11
s1=12
s2=13
s3=15
redpin=29
greenpin=31
bluepin=33

GPIO.setup(s0,GPIO.OUT)
GPIO.setup(s1,GPIO.OUT)
GPIO.setup(s2,GPIO.OUT)
GPIO.setup(s3,GPIO.OUT)
GPIO.setup(redpin,GPIO.OUT)
GPIO.setup(greenpin,GPIO.OUT)
GPIO.setup(bluepin,GPIO.OUT)


def TCS:
    flag=0
    GPIO.output(s0,GPIO.HIGH)
    GPIO.output(s1,GPIO.HIGH)
    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.LOW)
    GPIO.output(redpin,GPIO.LOW)
    GPIO.output(greenpin,GPIO.LOW)
    GPIO.output(bluepin,GPIO.LOW)
    
           








