import kasa
import asyncio

class KasaOutlet(object):

    def __init__(self, ipAddr):
        self.outlet = kasa.SmartPlug(ipAddr)
        self.turn_off()

    def turn_on():
        asyncio.run(self.outlet.turn_on())

    def turn_off():
        asyncio.run(self.outlet.turn_off())