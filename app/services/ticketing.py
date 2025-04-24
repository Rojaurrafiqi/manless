from escpos.printer import Usb
from datetime import datetime

class TicketPrinter:
    def __init__(self, id_vendor=0x04b8, id_product=0x0e15):
        # Ganti id_vendor dan id_product sesuai printer kamu (cek pakai `lsusb`)
        self.printer = Usb(id_vendor, id_product, 0)

    def print_ticket(self, vehicle_id: str):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.printer.set(align='center', text_type='B', width=2, height=2)
        self.printer.text("PARKIR OTOMATIS\n")
        self.printer.set(align='left', text_type='A', width=1, height=1)
        self.printer.text(f"Waktu masuk : {now}\n")
        self.printer.text(f"No. Kendaraan: {vehicle_id}\n")
        self.printer.text("\n")
        self.printer.text("Harap simpan tiket ini\n")
        self.printer.text("Tunjukkan saat keluar\n")
        self.printer.cut()

        print("[PRINTER] Tiket berhasil dicetak.")

