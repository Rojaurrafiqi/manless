from app.controller.gate_controller import GateController
from app.controller.sensor_handler import SensorHandler
from app.controller.button_handler import ButtonHandler
from app.controller.rfid_handler import RFIDHandler
from app.services.ticketing import TicketPrinter
from app.config import GATE_CONFIG
import pygame
import time

# Inisialisasi pygame mixer sekali
pygame.mixer.init()

def play_sound(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

def play_entry_sound():
    play_sound("app/sound/entry.wav")

def play_greeting_sound():
    play_sound("app/sound/greeting.wav")

def run_app():
    print("[INFO] Starting Barrier Gate App...")

    gate = GateController(GATE_CONFIG["gate_pin"])
    sensor = SensorHandler(GATE_CONFIG["loop1_pin"], GATE_CONFIG["loop2_pin"])
    button = ButtonHandler(GATE_CONFIG["button_pin"])
    rfid = RFIDHandler()
    printer = TicketPrinter()

    try:
        while True:
            if sensor.vehicle_on_loop1():
                print("[LOOP 1] Kendaraan berada di loop 1")
                play_entry_sound()

                # Tunggu aksi dari tombol atau RFID
                access_granted = False
                while sensor.vehicle_on_loop1() and not access_granted:
                    if button.is_pressed():
                        print("[BUTTON] Tombol tiket ditekan")
                        play_greeting_sound()
                        printer.print_ticket(vehicle_id="MANUAL-BUTTON")
                        access_granted = True

                    card_id = rfid.read_card()
                    if card_id:
                        print(f"[RFID] Kartu terdeteksi: {card_id}")
                        play_greeting_sound()
                        printer.print_ticket(vehicle_id=f"RFID-{card_id}")
                        access_granted = True

                    time.sleep(0.1)

                if access_granted:
                    gate.open()
                    print("[GATE] Gate terbuka, menunggu kendaraan di loop 2...")

                    while not sensor.vehicle_on_loop2():
                        time.sleep(0.1)
                    print("[LOOP 2] Kendaraan berada di loop 2")

                    # Tunggu sampai kendaraan benar-benar lewat
                    sensor.wait_until_passed_loop2()
                    gate.close()
                    print("[GATE] Gate tertutup")

            time.sleep(0.1)

    except KeyboardInterrupt:
        print("[INFO] Exiting application. Cleaning up GPIO.")
        gate.cleanup()
        sensor.cleanup()
