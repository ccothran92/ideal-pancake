from soil_sensor import SoilSensor
from plant import Plant
from soil import Soil
from watering_device import WateringDevice

myPlant = Plant(80, 1)
mySensor = SoilSensor(myPlant)

print(mySensor.needs_watering())
