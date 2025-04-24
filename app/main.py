from app.controller.gate_controller import GateController
from app.controller.sensor_handler import SensorHandler
from app.services.ticketing import TicketPrinter
from app.config import GATE_CONFIG

def run_app():
    print("[INFO] Starting Barrier Gate App...")

    gate = GateController(GATE_CONFIG["gate_pin"])
    sensor = SensorHandler(GATE_CONFIG["sensor_pin"])
    printer = TicketPrinter()

    try:
        while True:
            if sensor.vehicle_detected():
                print("[INFO] Vehicle detected. Opening gate...")
                
                gate.open()
                
                # Cetak tiket
                printer.print_ticket(vehicle_id="B 1234 XYZ")  # Ganti jika nanti ingin otomatis dari input/kamera
                
                sensor.wait_until_vehicle_passed()
                gate.close()

    except KeyboardInterrupt:
        print("[INFO] Exiting application. Cleaning up GPIO.")
        gate.cleanup()
        sensor.cleanup()
