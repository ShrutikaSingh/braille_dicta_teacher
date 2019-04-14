from socket import *
import RPi.GPIO as GPIO
import time

'''
import spidev,time                           	 #import SPI package/library
def lm_35():
 spi = spidev.SpiDev()                       	 #create object 
 spi.open(0,0)                                    #Initialise SPI
 def analog_read(channel):
   r = spi.xfer2([1, (8 + channel) << 4, 0])       #SPI transaction
   adc_out = ((r[1]&3) << 8) + r[2]                
   return adc_out
 while True:                                      
  reading = analog_read(0)                        
  voltage = reading * 5/1024                      #scaling factor                
  temp_c = voltage * 100
  temp_f = temp_c * 9.0 / 5.0 + 32                
  print("Temp C=%f\t\tTemp f=%f" % (temp_c, temp_f))
  time.sleep(1)
  return temp_c
''' 

HOST = '192.168.0.103'
PORT=8009
ISON_1 = 0
ISON_2 = 0

def main(p,conn):
    global ISON_1
    global ISON_2
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)
   # GPIO.setup(15,GPIO.OUT)
#-------------------------------------------------------------------------------------------#
    if(p=="a"):
        
        GPIO.output(11,True)
        ISON_1=1
        print "Bed Light ON"
        conn.send('HTTP/1.0 200 OK\r\n')
        conn.send("Content-Type: text/html\r\n\r\n")
        conn.send('{ "status": 200 , "device-type":11, "message" : "data recivied"}')
        conn.close()        
        
    if(p=="x"):
        
         if(ISON_1==1):
            conn.send('HTTP/1.0 200 OK\r\n')
            conn.send("Content-Type: text/html\r\n\r\n")
            conn.send('{ "status": 200 , "device-type":11, "message" : "data recivied"}')
          #  conn.send("ON")
            conn.close()

         if(ISON_1==0):
            conn.send('HTTP/1.0 200 OK\r\n')
            conn.send("Content-Type: text/html\r\n\r\n")
            conn.send('{ "status": 400 , "device-type":11, "message" : "data not recivied"}')
          #  conn.send("OFF")
            conn.close()

        
    if(p=="b"):
        GPIO.output(11,False)
        ISON_1 = -1
        conn.send('HTTP/1.0 200 OK\r\n')
        conn.send("Content-Type: text/html\r\n\r\n")
        conn.send('{ "status": 400 , "device-type":11, "message" : "data not recivied"}')
        conn.close()        

#--------------------------------------------------------------------------------------------#
    if(p=="c"):
        GPIO.output(13,True)
        ISON_2=1
        print "Bed fan ON"
        conn.send('HTTP/1.0 200 OK\r\n')
        conn.send("Content-Type: text/html\r\n\r\n")
        conn.send('{ "status": 200 , "device-type":13, "message" : "data recivied"}')
        conn.close()

    if(p=="y"):
        
         if(ISON_2==1):
            conn.send('HTTP/1.0 200 OK\r\n')
            conn.send("Content-Type: text/html\r\n\r\n")
            conn.send('{ "status": 200 , "device-type":13, "message" : "data recivied"}')
        #    conn.send("ON")
            conn.close()
            

         if(ISON_2==0):
            conn.send('HTTP/1.0 200 OK\r\n')
            conn.send("Content-Type: text/html\r\n\r\n")
            conn.send('{ "status": 400 , "device-type":13, "message" : "data not recivied"}')
         #   conn.send("OFF")
            conn.close()
            

        
        
    if(p=="d"):
        GPIO.output(13,False)
        ISON_2=0
        print "Bed off off"
        conn.send('HTTP/1.0 200 OK\r\n')
        conn.send("Content-Type: text/html\r\n\r\n")
        conn.send('{ "status": 400 , "device-type":13, "message" : "data recivied"}')
        conn.close()
         
#--------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------#


ss=socket(AF_INET,SOCK_STREAM)
ss.bind((HOST,PORT))
ss.listen(100)

while True:
    conn, add=ss.accept()

    str1=conn.recv(1024)
    
    print "Message:",str1
    print str1.split()

    data=str1.split()

    data1=data[1][4]
    print data1
    
   


    main(data1,conn)

'''   
conn.close()
ss.shutdown(SHUT_RDWR)
ss.close()
'''
