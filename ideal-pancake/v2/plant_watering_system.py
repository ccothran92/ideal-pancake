from soil_sensor import SoilSensor
from plant import Plant
from soil import Soil
from watering_device import WateringDevice
from plant_waterer import PlantWaterer
from kasa_outlet import KasaOutlet
from binary_soil_sensor import BinarySoilSensor
import time

SLEEP_TIME = 3

class PlantWateringSystem(object):
    def __init__(self, plant: Plant, watering_device: WateringDevice, sensor: SoilSensor):
        self.watering_device = watering_device
        self.plant_waterer = PlantWaterer(plant, sensor)
    
    def start(self):
        while True:
            if self.plant_waterer.needs_watering():
                self.watering_device.water_my_plants()
            else: 
                self.watering_device.dont_water_my_plants()
            time.sleep(SLEEP_TIME)


