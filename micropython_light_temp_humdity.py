from machine import Pin
from machine import ADC
from time import sleep
import dht

sensor = dht.DHT11(Pin(14))
adc = ADC(0)

while True:
  try:
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    light = adc.read()

    print('Temperature: %3.1f C' %temp)
    print('Humidity: %3.1f %%' %hum)
    print('Light: %3.1f' %light)
  except OSError as e:
    print('Failed to read sensor.')
