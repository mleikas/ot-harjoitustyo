import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(2500)
        self.assertEqual(str(self.maksukortti), "saldo: 35.0")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.maksukortti.ota_rahaa(250)
        self.assertEqual(str(self.maksukortti), "saldo: 7.5")

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertEqual("saldo: 10.0", str(self.maksukortti))
     
