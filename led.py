import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

button_pin = 17
led_pin = 27
led_pin1 = 22
led_pin2 = 23
pins = [led_pin,led_pin1,led_pin2]

button_pin2 = 26
led_pin3 = 16
led_pin4 = 6
led_pin5 = 5
pins2 = [led_pin3,led_pin4,led_pin5]

GPIO.setup(button_pin2, GPIO.IN)
GPIO.setup(led_pin3, GPIO.OUT)
GPIO.setup(led_pin4, GPIO.OUT)
GPIO.setup(led_pin5, GPIO.OUT)

GPIO.setup(button_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

led_number = 0
led_number2 = 0

def turn_on_led():
  global led_number
  GPIO.output(pins[led_number], GPIO.HIGH)
  led_number += 1

def turn_off_led():
  for pin in pins:
   GPIO.output(pin, GPIO.LOW)

def turn_on_led2():
  global led_number2
  GPIO.output(pins2[led_number2], GPIO.HIGH)
  led_number2 += 1

def turn_off_led2():
  for pin2 in pins2:
   GPIO.output(pin2, GPIO.LOW)

try:
   while True:
    if GPIO.input(button_pin) == GPIO.HIGH:
     if led_number < len(pins):
      turn_on_led()
      time.sleep(0.2)
      if led_number == len(pins):
       turn_off_led()
       led_number = 0
    if GPIO.input(button_pin2) == GPIO.HIGH:
     if led_number2 < len(pins2):
      turn_on_led2()
      time.sleep(0.2)
      if led_number2 == len(pins2):
       turn_off_led2()
       led_number2 = 0

except KeyboardInterrupt:
  GPIO.cleanup()


