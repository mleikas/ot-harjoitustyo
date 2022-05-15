# Käyttöohje


## Ohjelman käynnistäminen
Ennen ohjelman käynnistämistä, asenna riippuvuudet yatzy-app repositoriossa komennolla:

```bash
poetry install
```

Tämän jälkeen ohjelma voidaan käynnistää komennolla:

```bash
poetry run invoke start
```

## Pelaaminen
Yatzy:ssä sinulle annetaan 5 noppaa, joita voit heittää kierroksella kolme kertaa.
Voit pitää haluamasi nopat seuraavalle kierrokselle painamalla nopan vieressä olevaa "Pidä noppa" painiketta.
Kolmannen heiton sinun täytyy valita jokin kombinaatio, josta saat pisteitä sen mukaan, mitä noppia sinulla on.
Kombinaatioita ovat seuraavat:

### Yläpuolen kombinaatiot/Vasemman puolen kombinaatiot
- Ykköset: 
	Kaikki nopat, jossa sinulla on silmälukuna 1.
- Kakkoset: 
	Kaikki nopat, jossa sinulla on silmälukuna 2.
- Kolmoset: 
	Kaikki nopat, jossa sinulla on silmälukuna 3.
- Neloset: 
	Kaikki nopat, jossa sinulla on silmälukuna 4.
- Viitoset: 
	Kaikki nopat, jossa sinulla on silmälukuna 5.
- Kuutoset: 
	Kaikki nopat, jossa sinulla on silmälukuna 6.

Jos pelaajalla on yläpuolen kombinaatioiden pisteistä yhteensä tai enemmän kuin 63 pelin lopussa, pelaaja saa bonuksen eli 50 extra pistettä.

### Alapuolen kombinaatiot/Oikean puolen kombinaatiot
- Kolmoisluku: 
	Kolme samaa silmälukua.
- Neloisluku: 
	Neljä samaa silmälukua.
- Pieni suora: 
	Neljä peräkkäistä silmälukua. Esim. [2, 3, 4, 5]
- Suuri suora: 
	Viisi peräkkäistä silmälukua. Esim. [1, 2, 3, 4, 5]
- Täyskäsi/Full House: 
	Kolme samaa silmälukua ja kaksi jotain muuta silmälukua.
- Yatzy: 
	Viisi samaa silmälukua.
- Sattuma: 
	Mitkä tahansa silmäluvut nopissa. Näiden pisteet kerätään yhteen.

Kombinaatiot pidät painamalla kombinaation napiketta. Punaisena pidetyt voidaan heittää uudestaan, vihreänä pidetyt pysyvät samoina.

## Pelin lopetus

Peli loppuu, kun kaikki kombinaatiot ovat käyty.

Tämän jälkeen saat viestin, missä näkyvät keräämät pisteesi.
