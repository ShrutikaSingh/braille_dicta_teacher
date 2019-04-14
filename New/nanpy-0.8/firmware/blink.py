#!/usr/bin/env python

# Author: Andrea Stagi <stagi.andrea@gmail.com>
# Description: keeps your led blinking
# Dependencies: None

from nanpy import Arduino
sys.path.append('/home/pi/Desktop/nanpy-0.8/firmware/ArduinoClass.h')

Arduino.pinMode(4, Arduino.OUTPUT)

for i in range(10000):
    Arduino.digitalWrite(4, (i + 1) % 2)
    Arduino.delay(1000)

