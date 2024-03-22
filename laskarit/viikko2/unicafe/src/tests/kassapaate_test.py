import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


#Luodun kassapäätteen rahamäärä ja myytyjen lounaiden määrä on oikea (rahaa 1000 euroa, lounaita myyty 0)

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.maksukortti = Maksukortti(10000)
		#self.kassa.edulliset = 0
		#self.kassa.maukkaat = 0
	
    def test_luotu_kassa_on_olemassa(self):
        self.assertNotEqual(self.kassa, None)
    
    def test_kassapaatteen_rahamaara_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def testi_myytyjen_lounaiden_maara_on_oikea(self):
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)
        
#Käteisosto toimii sekä edullisten että maukkaiden lounaiden osalta
#Jos maksu riittävä: kassassa oleva rahamäärä kasvaa lounaan hinnalla ja vaihtorahan suuruus on oikea
#Jos maksu on riittävä: myytyjen lounaiden määrä kasvaa
#Jos maksu ei ole riittävä: kassassa oleva rahamäärä ei muutu, kaikki rahat palautetaan vaihtorahana ja myytyjen lounaiden määrässä ei muutosta
    def test_kateinen_maukkaalle_riittaa(self): 
        vaihtoraha= self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(vaihtoraha,0)
    	
        #self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
        self.assertEqual(self.kassa.maukkaat, 1)
    
    def test_kateinen_maukkaalle_ei_riita(self):
        vaihtoraha= self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(vaihtoraha,200)
    	
        self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)   
    
    def test_kateinen_edulliselle_riittaa(self):
        vaihtoraha= self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(vaihtoraha,0)
    	
        #self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(self.kassa.edulliset, 1) 
    
    def test_kateinen_edulliselle_ei_riita(self):
    
        vaihtoraha= self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha,200)
    	
        self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0) 

#Korttiosto toimii sekä edullisten että maukkaiden lounaiden osalta
#Jos kortilla on tarpeeksi rahaa, veloitetaan summa kortilta ja palautetaan True
#Jos kortilla on tarpeeksi rahaa, myytyjen lounaiden määrä kasvaa
#Jos kortilla ei ole tarpeeksi rahaa, kortin rahamäärä ei muutu, myytyjen lounaiden määrä muuttumaton ja palautetaan False
#Kassassa oleva rahamäärä ei muutu kortilla ostettaessa
        
    def test_korttisto_maukkaalle(self):
        kortti = Maksukortti(1000)
        self.assertEqual(kortti.saldo, 1000)

        peri_maksu = self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(peri_maksu, True)

        #self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        

    def test_korttisto_maukkaalle_ei_riita(self):

        kortti = Maksukortti(100)

        peri_maksu = self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)

        self.assertEqual(peri_maksu, False)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

        #self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.maukkaat, 0)
    


    def test_korttisto_edulliselle(self):

        kortti = Maksukortti(1000)
        self.assertEqual(kortti.saldo, 1000)

        peri_maksu = self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(peri_maksu, True)

        #self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_korttisto_edulliselle_ei_riita(self):

        kortti = Maksukortti(100)

        peri_maksu = self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)

        self.assertEqual(peri_maksu, False)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

        #self.kassa.syo_edullisesti_kortilla(kortti)kutsu
        self.assertEqual(self.kassa.edulliset, 0)

#Kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva rahamäärä kasvaa ladatulla summalla
    def test_kortille_rahaa_ladattaessa_kortin_saldo_muuttuu_ja_kassassa_oleva_rahamaara_kasvaa(self): 
        kortti = Maksukortti(100)
        print(kortti)
        

        self.kassa.lataa_rahaa_kortille(kortti, 500)  
        self.assertEqual(kortti.saldo, 600)
        self.assertEqual(self.kassa.kassassa_rahaa, 100500)
        print(kortti)
    

    def test_ladattaessa_neg_kortille(self):
        kortti = Maksukortti(100)

        self.kassa.lataa_rahaa_kortille(kortti, -500)  
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(kortti.saldo,100)

    def test_ladattaessa_nolla_kortille(self):
        kortti= Maksukortti(100)

        self.kassa.lataa_rahaa_kortille(kortti, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(kortti.saldo,100)


    def test_kassassa_rahaa_euroina(self):

        #self.kassa.kassassa_rahaa_euroina, 100000

        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000)



         

        
    



