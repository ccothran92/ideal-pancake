import kasa
import asyncio

class KasaOutlet(object):

    def __init__(self, ipAddr):
        self.outlet = kasa.SmartPlug(ipAddr)
        print(self.outlet.state_information)
        self._turn_off()

    def water_my_plants(self):
        print("Attempting to water plants")
        self._turn_on()
    
    def dont_water_my_plants(self):
        print("Stopping the watering of plants")
        self._turn_off()

    def _turn_on(self):
        asyncio.run(self.outlet.turn_on())

    def _turn_off(self):
        asyncio.run(self.outlet.turn_off())
