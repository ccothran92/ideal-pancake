from gpiozero import DigitalInputDevice
from soil_sensor import SoilSensor

class BinarySoilSensor(SoilSensor):
    def __init__(self, gpioPin):
        self.sensor = DigitalInputDevice(gpioPin)

    def get_moisture_percentage(self):
        if self.sensor.is_active == True:
            return 100
        else:
             return 0

    def get_soil_state(self):
        return "sdasd"