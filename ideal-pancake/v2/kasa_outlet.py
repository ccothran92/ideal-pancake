import kasa
import asyncio

from gpiozero import LED

class KasaOutlet(object):

    def __init__(self, ipAddr):
        self.outlet = kasa.SmartPlug(ipAddr) #TODO Self discovery?
        # asyncio.run(self.outlet.update())


    def water_my_plants(self):
        print("Attempting to water plants")
        asyncio.run(self._turn_on())

    
    def dont_water_my_plants(self):
        print("Stopping the watering of plants")
        asyncio.run(self._turn_off())

    async def _turn_on(self):
        # await self.outlet.update()
        # if not self.outlet.is_on:
            await self.outlet.turn_on()

    async def _turn_off(self):
        # await self.outlet.update()
        # if self.outlet.is_on:
            await self.outlet.turn_off()
