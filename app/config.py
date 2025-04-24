# Konfigurasi pin GPIO, durasi timer, dll
GATE_CONFIG = {
    "gate_pin": 13,       # GPIO pin untuk mengontrol gate (relay/servo)
    "rfid_enabled": True,
    "loop1_pin": 27,  # sensor kendaraan sebelum portal
    "loop2_pin": 22   # sensor kendaraan setelah portal
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