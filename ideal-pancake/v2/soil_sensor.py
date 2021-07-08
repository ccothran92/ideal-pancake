from soil import Soil
from plant import Plant

class SoilSensor(object):
    def __init__(self, plant: Plant, sensor: BinarySoilSensor): #TODO: Is this an unnecessary layer of abstraction? Probably. But I want to decouple specific types of sensors from the acting on the data
        self.plant = plant
        self.sensor = sensor

    def needs_watering(self):
        soil = self._get_soil_state()
        if (self.plant.desiredMoisturePercentage < self.sensor.getMoistureContent()):
            return True
        return False
    
    def _get_soil_state(self):
        return 