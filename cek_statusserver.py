STATUS_AKTIF = "aktif"
STATUS_NON_AKTIF = "non-aktif"


class Server:
    def __init__(self, hostname, ipaddress, status=STATUS_AKTIF):
        self.hostname = hostname
        self.ipaddress = ipaddress
        self.status = status

    def cek_status(self):
        if self.status == STATUS_AKTIF:
            return "Kondisi Server Aktif"
        else:
            return ValueError("Status server tidak valid")

    def set_status(self, new_status):
        self.status = new_status
        print(f"Status server {self.hostname} diubah menjadi {self.status}")


def kelolahServer():
    server_web = Server("web-server", "192.168.8.110")
    print(server_web.cek_status())

    print("Mengubah status server...")
    server_web.set_status(STATUS_AKTIF)


# kelolahServer()

# Fungsi baru yang akan kita uji
def validasi_ip_address(ip_address):
    """
    Memvalidasi format dasar alamat IP.
    """
    parts = ip_address.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True
