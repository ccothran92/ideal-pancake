from gpiozero import DigitalInputDevice

class BinarySoilSensor(object):
    def __init__(self, gpioPin):
        self.sensor = DigitalInputDevice(gpioPin)

    def getMoistureContent():
        if sensor.is_active == True:
            return 100
        else:
             return 0

