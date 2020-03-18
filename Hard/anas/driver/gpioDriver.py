
#f = open("/sys/class/gpio/export","w")
#f.write("18")
#f.close()

gpioNumber = 18

d = open("/sys/class/gpio/gpio{}/direction".format(gpioNumber),"w")
d.write("in")
d.close()

#v = open("/sys/class/gpio/gpio18/value","w")
#v.write("0")
#v.close()
