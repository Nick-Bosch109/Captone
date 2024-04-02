import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

button_pin = 17
led_pin = 27
led_pin1 = 22
led_pin2 = 23
pins = [led_pin,led_pin1,led_pin2]

GPIO.setup(button_pin, GPIO.OUT)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)

led_number = 0

def turn_on_led():
  global led_number
  GPIO.output(pins[led_number], GPIO.HIGH)
  led_number += 1

def turn_off_led():
  for pin in pins:
   GPIO.output(pin, GPIO.LOW)


try:
   while True:
    if GPIO.input(button_pin) == GPIO.HIGH:

     if led_number < len(pins):
      turn_on_led()
      time.sleep(0.2)

      if led_number == len(pins):
       turn_off_led()
       led_number = 0

except keyboardinterrupt:
  GPIO.cleanup()


