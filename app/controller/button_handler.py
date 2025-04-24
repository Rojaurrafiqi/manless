try:
    import RPi.GPIO as GPIO
except ImportError:
    GPIO = None

import time

class ButtonHandler:
    def __init__(self, pin):
        self.pin = pin
        if GPIO:
            GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def is_pressed(self):
        if GPIO:
            return GPIO.input(self.pin) == GPIO.HIGH
        print("[MOCK BUTTON] Simulating button press (False)")
        return False
