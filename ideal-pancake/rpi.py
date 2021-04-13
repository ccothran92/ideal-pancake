import RPi.GPIO as GPIO
import time
import outlet

channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
pump_on = False
def checkStatus(channel):
    #print("input=" + str(GPIO.input(channel)))
    if GPIO.input(channel):
        print("No water detected, turning pump on")
        return ensure_pump_is_on()
    else:
        print("Water has been detected. The pump will be off")
        return ensure_pump_is_off()

def ensure_pump_is_on():
    print("Pump should be on, checking in 1s")
    pump_on = True
    outlet.turn_on()
    return 1


def ensure_pump_is_off():
    print("pump should be off, checking in 30s")
    outlet.turn_off()
    pump_on = False
    return 5

while True:
    check_again_in_seconds = checkStatus(channel)
    time.sleep(check_again_in_seconds)

