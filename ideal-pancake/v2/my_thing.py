from soil_sensor import SoilSensor
from plant import Plant
from soil import Soil
from watering_device import WateringDevice
from kasa_outlet import KasaOutlet
import time
SLEEP_TIME = 3

waterer = WateringDevice(KasaOutlet("192.168.1.2"))
myPlant = Plant(80, 1)
mySensor = SoilSensor(myPlant)

while True:
    if mySensor.needs_watering():
        waterer.water_my_plants()
    else: 
        waterer.dont_water_my_plants()
    time.sleep(SLEEP_TIME)

print(mySensor.needs_watering())
