from gpiozero import DigitalInputDevice

class BinarySoilSensor(SoilSensor):
    def __init__(self, gpioPin):
        self.sensor = DigitalInputDevice(gpioPin)

    def getMoistureContent(self):
        if self.sensor.is_active == True:
            return 100
        else:
             return 0

