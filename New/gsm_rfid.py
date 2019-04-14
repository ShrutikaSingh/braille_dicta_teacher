import serial
import time
import sys

count=0;
def read_rfid ():
 ser = serial.Serial ("/dev/ttyUSB0")       #Open named port 
 ser.baudrate = 9600                        #Set baud rate to 9600
 data = ser.read(12)                        #Read 12 characters from serial port to data
 ser.close ()                               #Close port
 return data                                #Return data

D={'bank': 1500, 'owner': 'yogesh',    'type': 1,  'vrn': 'MH15DV2329'}
J={'bank': 2000, 'owner': 'aniket',    'type': 2,  'vrn': 'MH12EX4648'}
M={'bank': 5000, 'owner': 'abhishek',  'type': 3,  'vrn': 'MH14DJ0007'}
N={'bank': 7000, 'owner': 'omkar',     'type': 4,  'vrn': 'MH11AK2229'}
O={'bank': 5000, 'owner': 'yatin',     'type': 3,  'vrn': 'MH14DJ1140'}


def main_rfid(myid):
     print('wait...')
     time.sleep(1)
     
     if(myid=='510028EC33A6'):
       print('yehhh..id match successfully..!!!')
       print('Name:',D['owner'])
       print('vehicle type:',D['type'])
       print('vrn:',D['vrn'])
       count=1
       D['bank']-=100 
       print('your remaining acc bal is=',D['bank'])
       return 1
   
     elif(myid=='510029ACEE3A'):
       print('yehhh..id match successfully..!!!')
       print('Name:',J['owner'])
       print('vehicle type:',J['type'])
       print('vrn:',J['vrn'])
       count=2
       J['bank']-=200
       print('your remaining acc bal is=',J['bank'])
       return 1

     elif(myid=='510029978669'):
       print('yehhh..id match successfully..!!!')
       print('Name:',M['owner'])
       print('vehicle type:',M['type'])
       print('vrn:',M['vrn'])
       count=3
       M['bank']-=300 
       print('your remaining acc bal is=',M['bank'])
       return 1


     elif(myid=='51002962C1DB'):     
       print('yehhh..id match successfully..!!!')
       print('Name:',N['owner'])
       print('vehicle type:',N['type'])
       print('vrn:',N['vrn'])
       count=4
       N['bank']-=500
       print('your remaining acc bal is=',N['bank'])
       return 1
     '''    
     else:
       print('sorry new user...')
       print('make cash payment...')
       return 0
     '''
    
class gsm():
    echo_on = 1
    def __init__(self,serialPort):
        self.serialPort = serialPort

    def sendCommand(self,at_com):
        self.serialPort.write(at_com + '\r')


    def getResponse(self):
        self.serialPort.flushInput()
        self.serialPort.flushOutput()
        if gsm.echo_on == 1:
            response = self.serialPort.readline()  # comment this line if echo off
        response = self.serialPort.readline()
        response = response.rstrip()
        return response


    def getPrompt(self):
        if gsm.echo_on == 1:
            response = self.serialPort.readline()  # comment this line if echo off
        if (self.serialPort.readline(1) == '>'):
            return True
        else:
            return False


    def sendMessage(self,phone_number, message):
        flag = False
        self.sendCommand('AT+CMGS=\"' + phone_number + '\"')
        time.sleep(2)
        print 'SUCCESS'
        self.serialPort.write(message)
        self.serialPort.write('\x1A')  # send messsage if prompt received
        flag = True

        time.sleep(5)
        return flag

    def readMessage(self):
        flag = False
        message = ''
        self.sendCommand('AT+CMGR=1')
        self.serialPort.flushInput()
        self.serialPort.flushOutput()
        self.serialPort.readline().rstrip()
        while True:
            response = self.serialPort.readline().rstrip()
            if len(response)>1:
                if response == 'OK':
                    break
                else:
                    message = message +" " + response
                    flag = True

        return flag,message
        # response = self.getResponse().rstrip()
        # if response == 'OK':
        #     flag = False
        # else:
        #     message = self.serialPort.readline().rstrip()
        #     flag = True
        #
        # return flag,message

if __name__ == "__main__":
    gsm_ser = serial.Serial()
    gsm_ser.port = "/dev/ttyAMA0"
    gsm_ser.baudrate = 9600
    gsm_ser.timeout = 3
    gsm_ser.xonxoff = False
    gsm_ser.rtscts = False
    gsm_ser.bytesize = serial.EIGHTBITS
    gsm_ser.parity = serial.PARITY_NONE
    gsm_ser.stopbits = serial.STOPBITS_ONE

    try:
        gsm_ser.open()
        gsm_ser.flushInput()
        gsm_ser.flushOutput()
    except:
        print 'Cannot open serial port'
        sys.exit()

    GSM = gsm(gsm_ser)
    '''
    GSM.sendCommand("AT+IPR=9600;&W")
    print GSM.getResponse()

    time.sleep(.1)
    '''
    
    GSM.sendCommand("AT+CMGF=1;&W")
    print GSM.getResponse()

    time.sleep(.1)
    
    GSM.sendCommand("AT+CREG?")
    print GSM.getResponse()

    time.sleep(.1)
    




while True:
 
 
 id = read_rfid ()                          #Function call
 id=id.decode("utf-8")
 print(id)
 tag=main_rfid(id)
 print (tag)
 if (tag==1):
    status,msg = GSM.readMessage()
    if status == 0:
       print 'no new messages'
    else:
       print 'new messages arrived: ' + msg
    
    if (GSM.sendMessage("8237280950", M['bank']) == True):
       print 'Message sending Success'
    else:
       print 'Message sending Failed'
       time.sleep(.1)
    gsm_ser.close()








