#from ClassDriverGSEII.Classes import MyPin

#p = MyPin(18)
# p.export()
#print(p.direction)
#p.direction = "out"
#print(p.direction)

#p.value = 0

# Test ultrasound

from  ClassDriverGSEII.ultrasoundClass import Ultrasound
u = Ultrasound(14,15)
print(u.distance())
