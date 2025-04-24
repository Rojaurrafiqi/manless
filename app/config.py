# Konfigurasi pin GPIO, durasi timer, dll
GATE_CONFIG = {
    "gate_pin": 13,       # GPIO pin untuk mengontrol gate (relay/servo)
    "sensor_pin": 22,     # GPIO pin untuk loop detector atau sensor IR
    "rfid_enabled": True
}



"""
gpio pin 2 = (sda)
gpio pin 3 = (scl)
gpio 14 = (txd)
gpio 18 = (pcm clk)
gpio 22
gpio 9 (mso)
gpio 5
gpio 13 (pwm)
"""