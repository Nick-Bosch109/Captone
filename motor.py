import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

speed = 10
d1 = 9
d2 = 11

GPIO.setup(speed,GPIO.OUT)
GPIO.setup(d1,GPIO.OUT)
GPIO.setup(d2,GPIO.OUT)
p = GPIO.PWM(speed,100)

x = 0

while x == 0:
 GPIO.output(d1, GPIO.HIGH)
 GPIO.output(d2, GPIO.LOW)
 p.start(100)
 time.sleep(5)
 GPIO.output(d1, GPIO.LOW)
 GPIO.output(d2, GPIO.LOW)
 GPIO.output(speed, GPIO.LOW)
