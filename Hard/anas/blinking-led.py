import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT,initial=GPIO.LOW)

while True :
	GPIO.output(8,True)
	time.sleep(2)
	GPIO.output(8,False)
	time.sleep(2)

