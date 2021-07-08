from plant_watering_system import PlantWateringSystem
from kasa_outlet import KasaOutlet
from plant import Plant
from binary_soil_sensor import BinarySoilSensor

waterer = KasaOutlet("192.168.1.2")
myPlant = Plant(80, 1)
mySensor = BinarySoilSensor(26)

watering_system_1 = PlantWateringSystem(plant, waterer, mySensor)
watering_system_1.start()