from kasa_outlet import KasaOutlet

class WateringDevice(object):

    def __init__(self, device: KasaOutlet): #should be extendable to not just be kasa. i.e. gpio out
        self.device = device

    def water_my_plants():
        print("Attempting to water plants")
        self.device.turn_on()
    
    def dont_water_my_plants():
        print("Stopping the watering of plants")
        self.device.turn_off()