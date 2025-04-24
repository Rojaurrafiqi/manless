<!-- Dokumentasi proyek

app/config.py ====> Konfigurasi pin GPIO, durasi timer, dll
app/services  ====> Logika seperti QR scanner, ticketing, dll
app/controller  ====> pengotrol hardware
app/main.py  ====> Entry point aplikasi



untuk awal kali setup maka install dependency dengan cara
pip freeze > requirements.txt


Tips Debug Printer
Pastikan user pi punya akses ke USB: sudo usermod -a -G lp pi

Tes koneksi dengan script sederhana:
from escpos.printer import Usb
p = Usb(0x04b8, 0x0e15, 0)
p.text("Hello World\n")
p.cut()










Jalankan otomatis saat boot di raspberry
Menggunakan crontab:
crontab -e
Tambahkan baris:
@reboot python3 /home/pi/barrier_gate_app/run.py










-->
