import time
import RPi.GPIO as GPIO


#Motor A
enableMotorA = 12
in1 = 10
in2 = 8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(enableMotorA, GPIO.OUT, initial=False)
GPIO.setup(in1, GPIO.OUT, initial=False)
GPIO.setup(in2, GPIO.OUT, initial=False)

#MotorB
enableMotorB = 11
in3 = 15
in4 = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(enableMotorA, GPIO.OUT, initial=False)
GPIO.setup(in3, GPIO.OUT, initial=False)
GPIO.setup(in4, GPIO.OUT, initial=False)

