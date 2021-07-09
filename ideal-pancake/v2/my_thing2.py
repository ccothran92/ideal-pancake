from plant_watering_system import PlantWateringSystem
from kasa_outlet import KasaOutlet
from plant import Plant
from binary_soil_sensor import BinarySoilSensor

waterer2 = KasaOutlet("192.168.1.25")
myPlant2 = Plant(80, 1)
mySensor2 = BinarySoilSensor(2)
watering_system_2 = PlantWateringSystem(myPlant2, waterer2, mySensor2)
watering_system_2.start()