import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        self.maksukortti2 = Maksukortti(200)
        self.saldo = 1000

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")

    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(self.saldo)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100240")

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(self.saldo)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100400")

    def test_syo_edullisesti_nostaa_myytyjen_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(self.saldo)
        self.assertEqual(str(self.kassapaate.edulliset), "1")

    def test_syo_maukkaasti_nostaa_myytyjen_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(self.saldo)
        self.assertEqual(str(self.kassapaate.maukkaat), "1")

    def test_ei_riittavasti_rahaa_ei_muuta_kassan_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(20)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100000")
    
    def test_ei_riittavasti_rahaa_ei_muuta_myytyjen_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(20)
        self.assertEqual(str(self.kassapaate.maukkaat), "0")

    def test_korttiosto_toimii_edullisesti_ja_palautetaan_true(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_korttiosto_edullisesti_nostaa_lounaiden_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate.edulliset), "1")

    def test_korttiosto_toimii_maukkaasti_ja_palautetaan_true(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_korttiosto_maukkaasti_nostaa_lounaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.kassapaate.maukkaat), "1")

    def test_saldo_ei_mene_negatiiviseksi_ja_myydyt_pysyvat_samana(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti2)  
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti2), False)           
        self.assertEqual(str(self.kassapaate.maukkaat), "0")
    
    def test_saldo_kortissa_ja_kassassa_muuttuvat(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(self.maksukortti.saldo, 1200)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), "100200")