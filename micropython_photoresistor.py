from machine import ADC
adc = ADC(0)
while True:
    print(adc.read())
