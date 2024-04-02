import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

button1 = 17
led1 = 27

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(button1, GPIO.OUT)

while True:

 if GPIO.input(button1) == GPIO.HIGH:
  GPIO.output(led1, GPIO.HIGH)
 else:
  GPIO.output(led1, GPIO.LOW)


GPIO.cleanup()

