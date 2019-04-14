#import RPi.GPIO as GPIO
#import serial
#import time,os
from nanpy import SerialManager


def read_rfid():
  connection=SerialManager()
  #ser.baudrate=9600
  data=connection.readline()
  #ser.close()
  return data

id=read_rfid()
print id
 
