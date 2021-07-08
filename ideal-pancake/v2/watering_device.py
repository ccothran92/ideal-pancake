from abc import ABC, abstractmethod

class WateringDevice(ABC):

    def __init__(self):
        super(WateringDevice, self).__init__()
    
    @abstractmethod
    def water_my_plants(self):
        pass

    @abstractmethod
    def dont_water_my_plants(self):
        pass