from select import poll, POLLPRI
import time
parameters = {
  "w1_enabled": 1,
  "w1_pulse_width_min": 20,
  "w1_pulse_width_max": 100,
  "w1_pulse_itvl_min":200,
  "w1_pulse_itvl_max":20000
}
param = list(parameters.values())

file = [open("/sys/class/ionopi/wiegand/w1_enabled",'w'), open("/sys/class/ionopi/wiegand/w1_pulse_width_min",'w'), open("/sys/class/ionopi/wiegand/w1_pulse_width_max",'w'),
         open("/sys/class/ionopi/wiegand/w1_pulse_itvl_min",'w'), open("/sys/class/ionopi/wiegand/w1_pulse_itvl_max",'w')]

for i in range(0, len(parameters)):
    file[i].write(str(param[i]))

f = open("/sys/class/ionopi/wiegand/w1_data", "r")
p = poll()
p.register(f.fileno(), POLLPRI)
f.read()

while True:
    print("Waiting for card to scan.........")
    p.poll()
    time.sleep(0.5)

    # consume event
    f.seek(13)
    scanData = format(int(f.read()) , '026b')
    f_code = int(scanData[1:9] , 2)
    card_number = int(scanData[10:25] , 2)
    print("Facility Code =", f_code)
    print("Card Number = " , card_number)

