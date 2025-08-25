# test_app.py

import unittest
from cek_statusserver import (
    Server,
    validasi_ip_address,
    STATUS_AKTIF,
    STATUS_NON_AKTIF
)


class TestServer(unittest.TestCase):

    def test_status_default(self):
        """Menguji status default server."""
        server = Server("test-server", "1.1.1.1")
        self.assertEqual(server.status, STATUS_AKTIF)

    def test_set_status_nonaktif(self):
        """Menguji perubahan status server menjadi non-aktif."""
        server = Server("test-server", "1.1.1.1")
        server.set_status(STATUS_NON_AKTIF)
        self.assertEqual(server.status, STATUS_NON_AKTIF)


class TestFungsiValidasi(unittest.TestCase):

    def test_ip_valid(self):
        """Menguji alamat IP yang valid."""
        self.assertTrue(validasi_ip_address("192.168.1.1"))
        self.assertTrue(validasi_ip_address("127.0.0.1"))

    def test_ip_tidak_valid(self):
        """Menguji alamat IP yang tidak valid."""
        self.assertFalse(validasi_ip_address("192.168.1"))  # Kurang bagian
        self.assertFalse(validasi_ip_address("192.168.1.256"))  # Melebihi 255
        self.assertFalse(validasi_ip_address("a.b.c.d"))  # Bukan angka
        self.assertFalse(validasi_ip_address(
            "192.168.1.1.1"))  # Terlalu panjang


if __name__ == '__main__':
    unittest.main()
