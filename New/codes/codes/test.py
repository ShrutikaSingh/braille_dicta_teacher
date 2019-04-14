from socket import *
import RPi.GPIO as GPIO
import time

HOST = '192.168.0.120'
PORT=8009
ISON = 0

def main(p,conn):
    global ISON
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(15,GPIO.OUT)
    if(p=="a"):
        
        g=GPIO.output(11,True)
        ISON=1
        print "Bed Light ON"
        conn.send('HTTP/1.0 200 OK\r\n')
        conn.send("Content-Type: text/html\r\n\r\n")
        conn.send('{ "status": 200 , "message" : "data recivied"}')
        conn.close()        
        
    if(p=="x"):
        
         if(ISON==1):
            conn.send('HTTP/1.0 200 OK\r\n')
            conn.send("Content-Type: text/html\r\n\r\n")
            conn.send('{ "status": 200 , "message" : "data recivied"}')
            conn.close()

         if(ISON==0):
            conn.send('HTTP/1.0 200 OK\r\n')
            conn.send("Content-Type: text/html\r\n\r\n")
            conn.send('{ "status": 400 , "message" : "data recivied"}')
            conn.close()

        
    if(p=="b"):
        GPIO.output(11,False)
        ISON = -1
        conn.send('HTTP/1.0 200 OK\r\n')
        conn.send("Content-Type: text/html\r\n\r\n")
        conn.send('{ "status": 400 , "message" : "data recivied"}')
        conn.close()        

    if(p=="c"):
        GPIO.output(18,True)
        print "Bed fan ON"
    if(p=="d"):
        GPIO.output(18,False)
        print "Bed off off"
        

ss=socket(AF_INET,SOCK_STREAM)
ss.bind((HOST,PORT))
ss.listen(10)

while True:
    conn, add=ss.accept()

    str1=conn.recv(1024)
    
    print "Message:",str1
    print str1.split()
    data=str1.split()

    data1=data[1][4]
    print data1
    
   


    main(data1,conn)

  #while True:
       
#conn.close()
#ss.shutdown(SHUT_RDWR)
#ss.close()
