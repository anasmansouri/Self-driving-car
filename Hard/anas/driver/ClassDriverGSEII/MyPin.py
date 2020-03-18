class MyPin:

    def __init__(self, GpioNumber):
        self._GpioNumber = GpioNumber
        self._direction = "anas"
        self._value = None

    # direction
    @property
    def direction(self):
        print("getter of direction")
        return self._direction

    @direction.setter
    def direction(self, direction):
        print("on a changer la direction ")
        d = open("/sys/class/gpio/gpio{}/direction".format(self._GpioNumber), "w")
        d.write("{}".format(direction))
        d.close()
        self._direction = direction


    # value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        v = open("/sys/class/gpio/gpio{}/value".format(self._GpioNumber), "w")
        v.write("{}".format(self._value))
        v.close()

    # export gpio
    def export(self):
        f = open("/sys/class/gpio/export", "w")
        f.write("{}".format(self._GpioNumber))
        f.close()

    # enable pin - diretion - status

    def __repr__(self):
        return "MyPin(GpioNumber : {} ,direction : {} ,value : {})".format(self._GpioNumber,
                                                                           self.value,
                                                                           self.direction,
                                                                           )

    @staticmethod
    def description():
        return "this is a GpioDriver"