import spidev, time

spi = spidev.SpiDev()
spi.open(0,0)
def analog_read(channel):
 r = spi.xfer2([1, (8 + channel) << 4, 0])
 adc_out = ((r[1]&3) << 8) + r[2]
 return adc_out
while True:
 reading = analog_read(0)
 print("analog_read = %d\n" % (reading))
 print(reading)
 voltage = reading * 5.0 / 1024      #10 bit adc 2^10=1024 samples
 temp_c = voltage * 100
 temp_f = temp_c * 9.0 / 5.0 + 32
 print("Temp C=%f\t\tTemp f=%f" % (temp_c, temp_f))
 time.sleep(1)
