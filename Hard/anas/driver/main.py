from ClassDriverGSEII import MyPin

pin = MyPin.MyPin(18)
# pin.export()
print(pin.direction)

pin.direction="out"
print(pin.direction)

