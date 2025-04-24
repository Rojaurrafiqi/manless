try:
    import RPi.GPIO as GPIO
    from mfrc522 import SimpleMFRC522
except ImportError:
    # Untuk testing di PC
    SimpleMFRC522 = None

class RFIDHandler:
    def __init__(self):
        if SimpleMFRC522:
            self.reader = SimpleMFRC522()

    def read_card(self):
        if not self.reader:
            print("[MOCK RFID] Simulated card read")
            return "1234567890"
        
        print("[RFID] Waiting for card...")
        id, text = self.reader.read()
        print(f"[RFID] Detected card ID: {id}")
        return str(id)
