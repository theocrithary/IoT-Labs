from machine import Pin
ledPin = 14 # define ledPin
buttonPin = 13 # define buttonPin

print ('Program is starting...')
led = Pin(ledPin, Pin.OUT)
push_button = Pin(buttonPin, Pin.IN)

while True:
  logic_state = push_button.value()
  if logic_state == True:     # if pressed the push_button
      led.value(1)             # led will turn ON
  else:                       # if push_button not pressed
      led.value(0)             # led will turn OFF
