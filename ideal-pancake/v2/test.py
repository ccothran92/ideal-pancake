import time
import outlet
from gpiozero import DigitalInputDevice

channel = 26
device = DigitalInputDevice(channel)



pump_on = False
def checkStatus(channel):
    if  device.is_active == False:
        return ensure_pump_is_on()
    else:
        #print("Water has been detected. The pump will be off")
       # print("ACTIVE")
        print(device.value)
        return ensure_pump_is_off()

def ensure_pump_is_on():
    pump_on = True
    outlet.turn_on()
    return 1


def ensure_pump_is_off():
    outlet.turn_off()
    pump_on = False
    return 3


device.when_activated = ensure_pump_is_on
device.when_deactivated = ensure_pump_is_off

while True:
    check_again_in_seconds = checkStatus(channel)
    time.sleep(check_again_in_seconds)