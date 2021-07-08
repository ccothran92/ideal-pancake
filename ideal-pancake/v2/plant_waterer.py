from soil import Soil
from plant import Plant
from soil_sensor import SoilSensor

class PlantWaterer(object):
    def __init__(self, plant: Plant, sensor: SoilSensor): #TODO: Is this an unnecessary layer of abstraction? Probably. But I want to decouple specific types of sensors from
        self.plant = plant
        self.sensor = sensor

    def needs_watering(self):
        return self.plant.desired_moisture_percentage < self.sensor.get_moisture_percentage()):