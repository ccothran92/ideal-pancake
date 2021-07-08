from plant_watering_system import PlantWateringSystem



waterer = KasaOutlet("192.168.1.2")
myPlant = Plant(80, 1)
mySensor = SoilSensor(myPlant, BinarySoilSensor(26))

watering_system_1 = PlantWateringSystem(plant, waterer, mySensor)
watering_system_1.start()