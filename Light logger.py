
import Adafruit_BBIO.ADC as adc
import Adafruit_BBIO.GPIO as gpio
import time

led = 'P8_10'
sen = 'P9_40'

gpio.setup(led, gpio.OUT)
adc.setup()

while True:
        gpio.output(led, gpio.HIGH)
        reading = adc.read(sen)
        volts = reading * 1.800
        time.sleep(0.5)
        gpio.output(led, gpio.LOW)
        print('%f\t%f' % (reading, volts))
        time.sleep(0.5)
