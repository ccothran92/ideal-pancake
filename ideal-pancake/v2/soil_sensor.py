from soil import Soil
from plant import Plant

class SoilSensor(object):
    def __init__(self, plant: Plant):
        self.plant = plant

    def needs_watering(self):
        soil = self._get_soil_state()
        if (self.plant.desiredMoisturePercentage < soil.moistureContentPercentage):
            return True
        return False
    
    def _get_soil_state(self):
        return Soil(50)