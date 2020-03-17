import time
import RPi.GPIO as GPIO


class Motor:

    def __init__(self, motor_id, enable_pin, inl, inr, direction, status):
        self.motor_id = motor_id
        self.enable_pin = enable_pin
        self.direction = direction
        self.status = status
        self.inr = inr
        self.inl = inl
        if self.status == 0:
            GPIO.setup(self.enable_pin, GPIO.OUT, initial=False)
        else:
            GPIO.setup(self.enable_pin, GPIO.OUT, initial=True)
        if self.direction == 1:
            GPIO.setup(self.inr, GPIO.OUT, initial=True)
            GPIO.setup(self.inl, GPIO.OUT, initial=False)
        else:
            GPIO.setup(self.inr, GPIO.OUT, initial=False)
            GPIO.setup(self.inl, GPIO.OUT, initial=True)

    # motor_id
    @property
    def motor_id(self):
        return self.motor_id

    @motor_id.setter
    def motor_id(self, motor_id):
        self.motor_id = motor_id

    # enable pin

    @property
    def enable_pin(self):
        return self.enable_pin

    @enable_pin.setter
    def enable_pin(self, enable_pin):
        self.enable_pin = enable_pin

    # direction
    @property
    def direction(self):
        return self.direction

    @direction.setter
    def direction(self, direction):
        self.direction = direction
        self.update_parametres()

    # status
    @property
    def status(self):
        return self.status

    @status.setter
    def status(self, status):
        self.status = status
        self.update_parametres()

    # enable pin - diretion - status
    def update_parametres(self):
        if self.status == 1:
            GPIO.output(self.enable_pin, True)
        else:
            GPIO.output(self.enable_pin, False)

        if self.direction == 1:
            GPIO.output(self.inr, True)
            GPIO.output(self.inl, False)
        else:
            GPIO.output(self.inr, False)
            GPIO.output(self.inl, True)

    def __repr__(self):
        return "Motor(motor_id : {}\n,enable_pin : {}\n,direction : {}\n,status : {}\n".format(self.motor_id,
                                                                                               self.enable_pin,
                                                                                               self.direction,
                                                                                               self.status)
    @staticmethod
    def description():
        return "class Motor"
GPIO.setmode(GPIO.BOARD)
m = Motor("left",8,7,10,1,1)
while True:
    pass
