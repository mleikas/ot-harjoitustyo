# Testausdokumentti
Ohjelmaa on testattu automatisoiduin testien avulla unittestillä.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka ja luokat
Kaikki testattava on tiedostossa yatzy_test(./yatzy-app/src/tests/yatzy_test.py).

### Testauskattavuus
Testauksen haarautumakattavuus on 100%, koska koodissa on sekaisin logiikkaa ja käyttöliittymäkoodia.

## Järjestelmätestaus
Sovelluksen järjestelmätestaus on suoritettu manuaalisesti.

### Asennus ja konfigurointi
Käyttöohjeen(./dokumentaatio/kayttoohje.md) mukaisesti sovellusta on testattu Linux-ympäristössä.

### Toiminnallisuudet
Vaatimusmäärittelyn(./dokumentaatio/vaatimusmaarittely.md) listaamat toiminnot on käyty läpi. Kaikkia syötekenttiä/nappeja yritetty käyttää silloin, kun niitä ei pysty.


## Ongelmat
Ohjelmaa oli vaikeata testata, koska käyttölittymä koodia on niin paljon sekaisin.
