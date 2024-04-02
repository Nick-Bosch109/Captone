import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


button_pin = 17
led_pins = [27, 23, 24]
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

for led_pin in led_pins:
    GPIO.setup(led_pin, GPIO.OUT)

current_led_index = 0

def turn_on_next_led():
    global current_led_index
    GPIO.output(led_pins[current_led_index], GPIO.HIGH)
    current_led_index += 1

def turn_off_all_leds():
    for led_pin in led_pins:
        GPIO.output(led_pin, GPIO.LOW)

try:
 while True:
    if GPIO.input(button_pin) == GPIO.LOW:
     if current_led_index < len(led_pins):
      turn_on_next_led()
      time.sleep(0.2)
      if current_led_index == len(led_pins):
       turn_off_all_leds()
       current_led_index = 0

except KeyboardInterrupt:
   GPIO.cleanup()

