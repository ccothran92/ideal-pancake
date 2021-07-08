from abc import ABC, abstractmethod

class SoilSensor(ABC):

    def __init__(self):
        super(SoilSensor, self).__init__()
    
    @abstractmethod
    def get_moisture_percentage(self):
        pass
        