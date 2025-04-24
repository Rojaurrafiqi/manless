# Kontrol buka/tutup gate

import RPi.GPIO as GPIO
import time

class GateController:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def open(self):
        GPIO.output(self.pin, GPIO.HIGH)
        print("[GATE] Open signal sent")
        time.sleep(2)  # adjust this to duration of gate opening

    def close(self):
        GPIO.output(self.pin, GPIO.LOW)
        print("[GATE] Close signal sent")
        time.sleep(2)  # adjust this to duration of gate closing

    def cleanup(self):
        GPIO.cleanup(self.pin)
