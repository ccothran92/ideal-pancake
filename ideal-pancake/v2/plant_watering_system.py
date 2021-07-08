class PlantWateringSystem(object):
    def __init__()
    


from soil_sensor import SoilSensor
from plant import Plant
from soil import Soil
from watering_device import WateringDevice
from kasa_outlet import KasaOutlet
from binary_soil_sensor import BinarySoilSensor
import time

SLEEP_TIME = 3
KASA_IP = "192.168.1.2"
GPIO_PIN = 26

waterer = WateringDevice(KasaOutlet(KASA_IP))
myPlant = Plant(80, 1)
mySensor = SoilSensor(myPlant, BinarySoilSensor(26))

while True:
    if mySensor.needs_watering():
        waterer.water_my_plants()
    else: 
        waterer.dont_water_my_plants()
    time.sleep(SLEEP_TIME)

print(mySensor.needs_watering())
