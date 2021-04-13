import kasa
import asyncio
outlet = kasa.SmartPlug("192.168.1.21")
def turn_on():
    asyncio.run(outlet.turn_on())

def turn_off():
    asyncio.run(outlet.turn_off())
