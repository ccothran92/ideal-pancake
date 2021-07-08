from gpiozero import DigitalInputDevice
from soil_sensor import SoilSensor
from soil import Soil

class BinarySoilSensor(SoilSensor):
    def __init__(self, gpioPin):
        self.sensor = DigitalInputDevice(gpioPin)

    def get_soil_state(self)-> Soil:
        if self.sensor.is_active == True:
            soil_state = Soil(100)
        else:
            soil_state = Soil(0)
        return soil_state