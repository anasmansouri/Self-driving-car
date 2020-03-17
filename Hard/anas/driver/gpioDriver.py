
#f = open("/sys/class/gpio/export","w")
#f.write("18")
#f.close()

#d = open("/sys/class/gpio/gpio18/direction","w")
#d.write("out")
#d.close()

v = open("/sys/class/gpio/gpio18/value","w")
v.write("0")
v.close()
