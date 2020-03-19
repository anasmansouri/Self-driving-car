from ClassDriverGSEII.MyPin import MyPin

p = MyPin(18)
p.export()
print(p.direction)
p.direction = "out"
print(p.direction)
