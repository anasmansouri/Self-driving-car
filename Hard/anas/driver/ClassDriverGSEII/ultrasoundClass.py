
import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)


class Ultrasound:
    def __init__(self,triggerPinNumber,echoPinNumer):
        self.triggerPinNumber = triggerPinNumber
        self.echoPinNumer = echoPinNumer

    def distance(self):
        # set Trigger to HIGH
        GPIO.output(self.triggerPinNumber, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.triggerPinNumber, False)

        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        while GPIO.input(self.echoPinNumer) == 0:
            StartTime = time.time()

        # save time of arrival
        while GPIO.input(self.echoPinNumer) == 1:
            StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        return distance
