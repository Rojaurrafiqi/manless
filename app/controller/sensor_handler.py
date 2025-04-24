# Deteksi sensor (loop detector, infrared, dll)

import RPi.GPIO as GPIO
import time

class SensorHandler:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)

    def vehicle_detected(self):
        return GPIO.input(self.pin) == GPIO.HIGH

    def wait_until_vehicle_passed(self):
        print("[SENSOR] Waiting for vehicle to pass...")
        while GPIO.input(self.pin) == GPIO.HIGH:
            time.sleep(0.1)

    def cleanup(self):
        GPIO.cleanup(self.pin)
