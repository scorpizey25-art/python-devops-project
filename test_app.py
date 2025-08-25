import unittest
from app import tambah_angka


class Testfungsi(unittest.TestCase):

    def test_penjumlahan_positif(self):
        hasil = tambah_angka(5, 3)
        self.assertEqual(hasil, 8)

    def test_penjumlahan_negatif(self):
        hasil = tambah_angka(-10, -5)
        self.assertEqual(hasil, -15)


if __name__ == '__main__':
    unittest.main()
