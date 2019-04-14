import spidev, time

spi = spidev.SpiDev()
spi.open(0,0)
def analog_read(channel):
 r = spi.xfer2([1, (8 + channel) << 4, 0])
 adc_out = ((r[1]&3) << 8) + r[2]
 return adc_out
while True:
 reading = analog_read(0)
 print(reading)
 time.sleep(0.2)
 if reading >470 :
         print('alcohol detected...')
         time.sleep(0.2)
 else :
         print('not...')
         time.sleep(0.2)
 '''
 time.sleep(1)
 voltage = reading * 3.3/1024
 print(voltage)
 
 temp_c = voltage * 100
 temp_f = temp_c * 9.0 / 5.0 + 32
 print("Temp C=%f\t\tTemp f=%f" % (temp_c, temp_f))
 time.sleep(1)
'''
 
