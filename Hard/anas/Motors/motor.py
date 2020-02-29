import time
import RPi.GPIO as GPIO
# MotorA
enableMotorA = 12
in1 = 10
in2 = 8

#Motor B
enableMotorB = 11
in3 = 15
in4 = 13


# MotorA
GPIO.setmode(GPIO.BOARD)
GPIO.setup(enableMotorA, GPIO.OUT, initial=True)
GPIO.setup(in1, GPIO.OUT, initial=True)
GPIO.setup(in2, GPIO.OUT, initial=False)

#Motor B
GPIO.setmode(GPIO.BOARD)
GPIO.setup(enableMotorB, GPIO.OUT, initial=True)
GPIO.setup(in3, GPIO.OUT, initial=True)
GPIO.setup(in4, GPIO.OUT, initial=False)

while True:
    GPIO.output(in3, True)
    GPIO.output(in4, False)
    time.sleep(4)
    GPIO.output(in3,False)
    GPIO.output(in4,True)
    time.sleep(4)
