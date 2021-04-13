import RPi.GPIO as GPIO

class SoilSensor:
    def __init__(self, channel):
        GPIO.setup(channel, GPIO.IN)
        self.channel = channel

    def is_water_detected(self):
        return GPIO.input(self.channel)