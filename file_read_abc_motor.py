import time
import RPi.GPIO as GPIO

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



f = open('/home/pi/textabc.txt', 'r')               # f is file descriptor
c=f.read()# read the file using
for i in range(0,26):
    if c[i] == 'a':
        print c[i]
        print ("solonoid pin1 on")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        time.sleep(1)
    if c[i] == 'b':
        print c[i]
        print ("solonoid pin1 on")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        print ("solonoid pin3 on")
        GPIO.output(Motor3A,GPIO.HIGH)
        GPIO.output(Motor3B,GPIO.LOW)
        
        time.sleep(1)
        
    if c[i] == 'c':
        print c[i]
        print ("solonoid pin1 on")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        print ("solonoid pin2 on")
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        
        time.sleep(1)
    
    if c[i] == 'd':
        print c[i]
        print ("solonoid pin1 on")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        print ("solonoid pin2 on")
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        print ("solonoid pin4 on")
        GPIO.output(Motor4A,GPIO.HIGH)
        GPIO.output(Motor4B,GPIO.LOW)
        
        time.sleep(1)
    if c[i] == 'e':
        print c[i]
        print ("solonoid pin1 on")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        print ("solonoid pin4 on")
        GPIO.output(Motor4A,GPIO.HIGH)
        GPIO.output(Motor4B,GPIO.LOW)
        
        time.sleep(1)
    if c[i] == 'f':
        print c[i]
        print ("solonoid pin1 on")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)

        print ("solonoid pin2 on")
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        
        print ("solonoid pin3 on")
        GPIO.output(Motor3A,GPIO.HIGH)
        GPIO.output(Motor3B,GPIO.LOW)
        
        time.sleep(1)
    
    if c[i] == 'g':
        print c[i]
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
      
        time.sleep(1)
    
    if c[i] == 'h':
        print c[i]
        print ("solonoid pin1 on")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        
        print ("solonoid pin3 on")
        GPIO.output(Motor3A,GPIO.HIGH)
        GPIO.output(Motor3B,GPIO.LOW)
        
        print ("solonoid pin4 on")
        GPIO.output(Motor4A,GPIO.HIGH)
        GPIO.output(Motor4B,GPIO.LOW)
        
        time.sleep(1)
    if c[i] == 'i':
        print c[i]
        print ("solonoid pin2 on")
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        
        print ("solonoid pin3 on")
        GPIO.output(Motor3A,GPIO.HIGH)
        GPIO.output(Motor3B,GPIO.LOW)
        
       
        time.sleep(1)

    if c[i] == 'j':
        print c[i]
        print ("solonoid pin2 on")
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        
        print ("solonoid pin3 on")
        GPIO.output(Motor3A,GPIO.HIGH)
        GPIO.output(Motor3B,GPIO.LOW)
        
        print ("solonoid pin4 on")
        GPIO.output(Motor4A,GPIO.HIGH)
        GPIO.output(Motor4B,GPIO.LOW)
        
        
        time.sleep(1)
    if c[i] == 'k':
        print c[i]
        print ("solonoid pin1 on")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        print ("solonoid pin5 on")
        GPIO.output(Motor5A,GPIO.HIGH)
        GPIO.output(Motor5B,GPIO.LOW)
        
        
        time.sleep(1)
    
    if c[i] == 'l':
        print c[i]
        print ("solonoid pin1 on")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)

        print ("solonoid pin3 on")
        GPIO.output(Motor3A,GPIO.HIGH)
        GPIO.output(Motor3B,GPIO.LOW)

        print ("solonoid pin5 on")
        GPIO.output(Motor5A,GPIO.HIGH)
        GPIO.output(Motor5B,GPIO.LOW)
        
        
        time.sleep(1)
    if c[i] == 'm':
        print c[i]
        print ("solonoid pin1 on")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)

        print ("solonoid pin2 on")
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)

        print ("solonoid pin5 on")
        GPIO.output(Motor5A,GPIO.HIGH)
        GPIO.output(Motor5B,GPIO.LOW)
        
        
        time.sleep(1)
    if c[i] == 'n':
        print c[i]
        print ("solonoid pin1 on")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)

        print ("solonoid pin2 on")
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)

        print ("solonoid pin4 on")
        GPIO.output(Motor4A,GPIO.HIGH)
        GPIO.output(Motor4B,GPIO.LOW)

        print ("solonoid pin5 on")
        GPIO.output(Motor5A,GPIO.HIGH)
        GPIO.output(Motor5B,GPIO.LOW)
        
        
        time.sleep(1)
    if c[i] == 'o':
        print c[i]
        
        print ("solonoid pin1 on")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)

        
        print ("solonoid pin4 on")
        GPIO.output(Motor4A,GPIO.HIGH)
        GPIO.output(Motor4B,GPIO.LOW)

        print ("solonoid pin5 on")
        GPIO.output(Motor5A,GPIO.HIGH)
        GPIO.output(Motor5B,GPIO.LOW)
        

        time.sleep(1)

    if c[i] == 'p':
        print c[i]
        print ("solonoid pin1 on")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)

        print ("solonoid pin2 on")
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)

        print ("solonoid pin3 on")
        GPIO.output(Motor3A,GPIO.HIGH)
        GPIO.output(Motor3B,GPIO.LOW)

        print ("solonoid pin5 on")
        GPIO.output(Motor5A,GPIO.HIGH)
        GPIO.output(Motor5B,GPIO.LOW)
        
        
        time.sleep(1)
    if c[i] == 'q':
        print c[i]
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
        
       
        time.sleep(1)
    if c[i] == 'r':
        print c[i]
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
        
        
        time.sleep(1)
    if c[i] == 's':
        print c[i]
        print ("solonoid pin2 on")
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)

        print ("solonoid pin3 on")
        GPIO.output(Motor3A,GPIO.HIGH)
        GPIO.output(Motor3B,GPIO.LOW)
        
        
        print ("solonoid pin5 on")
        GPIO.output(Motor5A,GPIO.HIGH)
        GPIO.output(Motor5B,GPIO.LOW)
        
       
        time.sleep(1)
    if c[i] == 't':
        print c[i]
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
        
       
        time.sleep(1)
    if c[i] == 'u':
        print c[i]
        
        print ("solonoid pin1 on")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        print ("solonoid pin5 on")
        GPIO.output(Motor5A,GPIO.HIGH)
        GPIO.output(Motor5B,GPIO.LOW)
        print ("solonoid pin6 on")
        GPIO.output(Motor6A,GPIO.HIGH)
        GPIO.output(Motor6B,GPIO.LOW)
      
        time.sleep(1)
    if c[i] == 'v':
        print c[i]
        print ("solonoid pin1 on")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)

        print ("solonoid pin3 on")
        GPIO.output(Motor3A,GPIO.HIGH)
        GPIO.output(Motor3B,GPIO.LOW)
        print ("solonoid pin5 on")
        GPIO.output(Motor5A,GPIO.HIGH)
        GPIO.output(Motor5B,GPIO.LOW)
        print ("solonoid pin6 on")
        GPIO.output(Motor6A,GPIO.HIGH)
        GPIO.output(Motor6B,GPIO.LOW)
        
        
        
        time.sleep(1)
    if c[i] == 'w':
        print c[i]
        
        time.sleep(1)
    if c[i] == 'x':
        print c[i]
        
        print ("solonoid pin1 on")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)

        print ("solonoid pin2 on")
        GPIO.output(Motor3A,GPIO.HIGH)
        GPIO.output(Motor3B,GPIO.LOW)
        print ("solonoid pin5 on")
        GPIO.output(Motor5A,GPIO.HIGH)
        GPIO.output(Motor5B,GPIO.LOW)
        print ("solonoid pin6 on")
        GPIO.output(Motor6A,GPIO.HIGH)
        GPIO.output(Motor6B,GPIO.LOW)
        
        time.sleep(1)
    if c[i] == 'y':
        print c[i]
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
        
      
        time.sleep(1)
    if c[i] == 'z':
        print c[i]
        print ("solonoid pin1 on")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)

        print ("solonoid pin4 on")
        GPIO.output(Motor4A,GPIO.HIGH)
        GPIO.output(Motor4B,GPIO.LOW)
        print ("solonoid pin5 on")
        GPIO.output(Motor5A,GPIO.HIGH)
        GPIO.output(Motor5B,GPIO.LOW)

        print ("solonoid pin6 on")
        GPIO.output(Motor6A,GPIO.HIGH)
        GPIO.output(Motor6B,GPIO.LOW)
        
        time.sleep(1)


       
    


    

















