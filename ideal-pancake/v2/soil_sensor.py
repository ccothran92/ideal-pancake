from abc import ABC, abstractmethod
from soil import Soil

class SoilSensor(ABC):

    def __init__(self):
        super(SoilSensor, self).__init__()
    
    @abstractmethod
    def get_moisture_percentage(self):
        pass
        
    @abstractmethod
    def get_soil_state(self)-> Soil
        pass