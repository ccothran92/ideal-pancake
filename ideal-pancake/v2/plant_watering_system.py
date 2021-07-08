from soil_sensor import SoilSensor
from plant import Plant
from soil import Soil
from watering_device import WateringDevice
from kasa_outlet import KasaOutlet
from binary_soil_sensor import BinarySoilSensor
import time

SLEEP_TIME = 3

class PlantWateringSystem(object):
    def __init__(plant: Plant, watering_device: WateringDevice, sensor: SoilSensor):
        self.gpioPin = gpioPin
        self.watering_device = watering_device
        self.sensor = sensor

    def start(self):
        while True:
        if self.sensor.needs_watering():
            self.watering_device.water_my_plants()
        else: 
            self.watering_device.dont_water_my_plants()
        time.sleep(SLEEP_TIME)


