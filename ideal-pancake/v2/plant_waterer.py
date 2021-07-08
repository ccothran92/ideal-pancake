from soil import Soil
from plant import Plant
from soil_sensor import SoilSensor

class PlantWaterer(object):
    def __init__(self, plant: Plant, soilSensor: SoilSensor): #TODO: Is this an unnecessary layer of abstraction? Probably. But I want to decouple specific types of sensors from
        self.plant = plant
        self.soilSensor = soilSensor

    def needs_watering(self):
        return self.plant.desired_moisture_percentage < self.soilSensor.get_soil_state().moisture_percentage