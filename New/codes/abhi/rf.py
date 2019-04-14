import serial                              #import serial module
#import RPi.GPIO as GPIO
#GPIO.setmode(11)

def read_rfid ():
 ser = serial.Serial ("/dev/ttyAMA0")       #Open named port 
 ser.baudrate = 9600                        #Set baud rate to 9600
 ser.write('h')                        #Read 12 characters from serial port to data
 ser.close ()                               #Close port
 #return data                                #Return data

#while(1):
# id = read_rfid ()                          #Function call
# print(id)                                   #Print RFID


