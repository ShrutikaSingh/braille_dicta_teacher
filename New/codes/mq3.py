import spidev, time                          #includes multiple libraries
import signal,os                             #includes multiple libraries
count=0                                      #global variable
timer=0                                      #global variable
timeinseconds=0                              #global variable
n=0;                                         #global variable 
spi = spidev.SpiDev()                        #declare object for SpiDev library 
spi.open(0,0)                                #Connects to the specified SPI device

#function starts :
def analog_read(channel):                    #function definition starts
 r = spi.xfer2([1, (8 + channel) << 4, 0])   # 
 adc_out = ((r[1]&3) << 8) + r[2]            #
 return adc_out                              # return from function with value
 #function end


#infinite loop starts
while True:       
 reading = analog_read(0)                    #take return value of function in reading variable
 time.sleep(0.2)                             #delay of 20ms
 
 if reading >50 :                            #compare value with std  
         count=count+1
         print("gas detected")
         time.sleep(0.1)
 else :                                            
         print('gas not detected...')
         time.sleep(0.1)

