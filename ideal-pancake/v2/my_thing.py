from plant_watering_system import PlantWateringSystem
from kasa_outlet import KasaOutlet
from plant import Plant
from binary_soil_sensor import BinarySoilSensor

waterer = KasaOutlet("Ace")
myPlant = Plant(80, 1)
mySensor = BinarySoilSensor(26)

watering_system_1 = PlantWateringSystem(myPlant, waterer, mySensor)
watering_system_1.start()

