#import RPi.GPIO as GPIO
import serial
#import time,os

def read_rfid():
  ser=serial.Serial("/dev/ttyACM0")
  ser.baudrate=9600
  data=ser.read(12)
  ser.close()
  return data

while True:
 id=read_rfid()
 print id
 
