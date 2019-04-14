import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
#solonoid pin 1  
Motor1A = 11
Motor1B = 12
#solonoid pin2
Motor2A = 13
Motor2B = 15
#solonoid pin3
Motor3A = 16
Motor3B = 18
#solonoid pin4
Motor4A = 31
Motor4B = 32
#solonoid pin5
Motor5A = 35
Motor5B = 36
#solonoid pin6
Motor6A = 37
Motor6B = 38
#Motor1E = 15

#set up solonoid pin1 as output
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
#set up solonoid pin2 as output
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
#set up solonoid pin3 as output
GPIO.setup(Motor3A,GPIO.OUT)
GPIO.setup(Motor3B,GPIO.OUT)
#set up solonoid pin4 as output
GPIO.setup(Motor4A,GPIO.OUT)
GPIO.setup(Motor4B,GPIO.OUT)
#set up solonoid pin5 as output
GPIO.setup(Motor5A,GPIO.OUT)
GPIO.setup(Motor5B,GPIO.OUT)
#set up solonoid pin6 as output
GPIO.setup(Motor6A,GPIO.OUT)
GPIO.setup(Motor6B,GPIO.OUT)
#GPIO.setup(Motor1E,GPIO.OUT)
while True:     
    print ("solonoid pin1 on")
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)

    print ("solonoid pin2 on")
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)

    print ("solonoid pin3 on")
    GPIO.output(Motor3A,GPIO.HIGH)
    GPIO.output(Motor3B,GPIO.LOW)
    print ("solonoid pin4 on")
    GPIO.output(Motor4A,GPIO.HIGH)
    GPIO.output(Motor4B,GPIO.LOW)
    
    print ("solonoid pin5 on")
    GPIO.output(Motor5A,GPIO.HIGH)
    GPIO.output(Motor5B,GPIO.LOW)
    print ("solonoid pin6 on")
    GPIO.output(Motor6A,GPIO.HIGH)
    GPIO.output(Motor6B,GPIO.LOW)
    #GPIO.output(Motor1E,GPIO.HIGH)
     
    time.sleep(2)
     
    print ("solonoid pin1 off")
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)

    print ("solonoid pin2 off")
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)

    print ("solonoid pin3 off")
    GPIO.output(Motor3A,GPIO.LOW)
    GPIO.output(Motor3B,GPIO.HIGH)
    print ("solonoid pin4 off")
    GPIO.output(Motor4A,GPIO.LOW)
    GPIO.output(Motor4B,GPIO.HIGH)

    print ("solonoid pin5 off")
    GPIO.output(Motor5A,GPIO.LOW)
    GPIO.output(Motor5B,GPIO.HIGH)

    print ("solonoid pin6 off")
    GPIO.output(Motor6A,GPIO.LOW)
    GPIO.output(Motor6B,GPIO.HIGH)

    
    
    #GPIO.output(Motor1E,GPIO.HIGH)

    time.sleep(2)
     
    GPIO.cleanup()
