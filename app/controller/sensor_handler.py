import time

try:
    import RPi.GPIO as GPIO
except ImportError:
    GPIO = None

class SensorHandler:
    def __init__(self, loop1_pin, loop2_pin):
        self.loop1_pin = loop1_pin
        self.loop2_pin = loop2_pin

        if GPIO:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.loop1_pin, GPIO.IN)
            GPIO.setup(self.loop2_pin, GPIO.IN)

    def vehicle_on_loop1(self):
        if GPIO:
            return GPIO.input(self.loop1_pin) == GPIO.HIGH
        return False  # untuk testing di PC

    def vehicle_on_loop2(self):
        if GPIO:
            return GPIO.input(self.loop2_pin) == GPIO.HIGH
        return False

    def wait_until_passed_loop2(self):
        print("[INFO] Waiting for vehicle to pass loop 2...")
        while self.vehicle_on_loop2():
            time.sleep(0.1)
        print("[INFO] Vehicle passed.")

    def cleanup(self):
        if GPIO:
            GPIO.cleanup()
