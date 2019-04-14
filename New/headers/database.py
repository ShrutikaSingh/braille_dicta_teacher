import time
import RPi.GPIO as GPIO
import serial                              #import serial module

'''
count_1=0
count_2=0
count_3=0
count_4=0
count_5=0
count_6=0
'''

def read_rfid ():
 ser = serial.Serial ("/dev/ttyAMA0")       #Open named port 
 ser.baudrate = 9600                        #Set baud rate to 9600
 data = ser.read(12)                        #Read 12 characters from serial port to data
 ser.close ()                               #Close port
 return data                                #Return data

D={'bank': 1500, 'owner': 'yogesh',    'type': 1,  'vrn': 'MH15DV2329'}
J={'bank': 2000, 'owner': 'aniket',    'type': 2,  'vrn': 'MH12EX4648'}
M={'bank': 5000, 'owner': 'abhishek',  'type': 3,  'vrn': 'MH14DJ0007'}
N={'bank': 7000, 'owner': 'omkar',     'type': 4,  'vrn': 'MH11AK2229'}
O={'bank': 5000, 'owner': 'yatin',     'type': 3,  'vrn': 'MH14DJ1140'}

def main(myid):
     #M=[[b'510028EC33A6'],[b'510029ACEE3A'],[b'510029978669'],[b'51002962C1DB']]
     
     

     '''
     print(D)
     print(E)
     print(F)
     print(G)

     print(" ")
     print(M[1])
     print(M[2])
     
     b'510028EC33A6'=D
     b'510029ACEE3A'=J
     b'510029978669'=M
     b'51002962C1DB'=N
     b'51002931A8E1'=O
     b'51002CE9F460'=L
     
     x=input('Enter vehicle type:')

     
     '''

     
     print('wait...')
     time.sleep(1)
     
     if(myid=='510028EC33A6'):
       print('yehhh..id match successfully..!!!')
       print('Name:',D['owner'])
       print('vehicle type:',D['type'])
       print('vrn:',D['vrn'])
       
       D['bank']-=100 
       print('your remaining acc bal is=',D['bank'])
       
   
     elif(myid=='510029ACEE3A'):
       print('yehhh..id match successfully..!!!')
       print('Name:',J['owner'])
       print('vehicle type:',J['type'])
       print('vrn:',J['vrn'])
       
       J['bank']-=200
       print('your remaining acc bal is=',J['bank'])
 

     elif(myid=='510029978669'):
       print('yehhh..id match successfully..!!!')
       print('Name:',M['owner'])
       print('vehicle type:',M['type'])
       print('vrn:',M['vrn'])
       
       M['bank']-=300 
       print('your remaining acc bal is=',M['bank'])
 


     elif(myid=='51002962C1DB'):     
       print('yehhh..id match successfully..!!!')
       print('Name:',N['owner'])
       print('vehicle type:',N['type'])
       print('vrn:',N['vrn'])
       
       N['bank']-=500
       print('your remaining acc bal is=',N['bank'])
       
     else:
       print('sorry new user...')
       print('make cash payment...')
     

while True:
 id = read_rfid ()                          #Function call
 id=id.decode("utf-8")
 print(id)
 main(id)






'''
import serial                              #import serial module

def read_rfid ():
 ser = serial.Serial ("/dev/ttyAMA0")       #Open named port 
 ser.baudrate = 9600                        #Set baud rate to 9600
 data = ser.read(12)                        #Read 12 characters from serial port to data
 ser.close ()                               #Close port
 return data                                #Return data

while True:
  id = read_rfid ()                          #Function call
  print(id)                                   #Print RFID
'''
