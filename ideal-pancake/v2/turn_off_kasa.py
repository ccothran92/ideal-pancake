from kasa_outlet import KasaOutlet

kasa1 = KasaOutlet("192.168.1.2")
kasa1.dont_water_my_plants()

kasa2 = KasaOutlet("192.168.1.25")
kasa2.dont_water_my_plants()