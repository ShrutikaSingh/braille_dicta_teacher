'''
import serial
import time
def func():
  ser=serial.Serial('/dev/ttyUSB0',9600)
  a=ser.read(12)
  print(a)
  time.sleep(0.1)
  ser.close()

while True:
    id=func()
    print(id)
'''

import serial
#import RPi.GPIO as GPIO      
import os, time
num="8237280950" 
#GPIO.setmode(GPIO.BOARD)    
 
# Enable Serial Communication
port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)
 
# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key
 
port.write('AT'+'\r\n')
rcv = port.read(10)
print rcv
time.sleep(1)
''' 
port.write('ATE0'+'\r\n')      # Disable the Echo
rcv = port.read(10)
print rcv
time.sleep(1)
''' 
port.write('AT+CMGF=1'+'\r')  # Select Message format as Text mode 
rcv = port.read(10)
print rcv
time.sleep(1)
''' 
port.write('AT+CNMI=2,1,0,0,0'+'\r\n')   # New SMS Message Indications
rcv = port.read(10)
print rcv
time.sleep(1)
''' 
# Sending a message to a particular Number
 
port.write('AT+CMGS=\"'+num+'\"')
rcv = port.read(10)
print rcv
time.sleep(1)
 
port.write('Hello User'+'\n')  # Message
rcv = port.read(10)
print rcv
 
port.write("\x1A") # Enable to send SMS
for i in range(10):
    rcv = port.read(10)
    print rcv

