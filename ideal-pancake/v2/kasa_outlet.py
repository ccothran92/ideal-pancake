import kasa
import asyncio

class KasaOutlet(object):

    def __init__(self, ipAddr):
        self.outlet = kasa.SmartPlug(ipAddr)
        asyncio.run(self._state_info())
        self._turn_off()

    def water_my_plants(self):
        print("Attempting to water plants")
        self._turn_on()
    
    def dont_water_my_plants(self):
        print("Stopping the watering of plants")
        self._turn_off()

    async def _state_info(self):
        await self.outlet.update()
        print(self.outlet.state_information)

    async def _turn_on(self):
        # asyncio.run(_state_info)
        await self.outlet.update()
        await if not awaitself.outlet.is_on:
            await self.outlet.turn_on()

    def _turn_off(self):
        asyncio.run(self.outlet.turn_off())
