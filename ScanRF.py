from select import poll, POLLPRI

parameters = [1, 20, 100, 200, 20000]

file = [open("/sys/class/ionopi/wiegand/w1_enabled",'w'), open("/sys/class/ionopi/wiegand/w1_pulse_width_min",'w'), open("/sys/class/ionopi/wiegand/w1_pulse_width_max",'w'),
         open("/sys/class/ionopi/wiegand/w1_pulse_itvl_max",'w'), open("/sys/class/ionopi/wiegand/w1_pulse_itvl_min",'w')]

for i in range(0, len(parameters)):
    file[i].write(str(parameters[i]))

f = open("/sys/class/ionopi/wiegand/w1_data", "r")
p = poll()
p.register(f.fileno(), POLLPRI)
f.read()

while True:
    p.poll()

    # consume event
    f.seek(13)
    scanData = int(f.read())
    scanData1 = format(scanData , '026b')
    f_code = int(scanData1[1:9] , 2)
    card_number = int(scanData1[10:25] , 2)
    print("Facility Code =", f_code)
    print("Card Number = " , card_number)

