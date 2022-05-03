# Arkkitehtuurikuvaus

## Käyttöliittymä
Käyttöliittymässä on kaksi erillistä näkymää:
- Pelin käyttöliittymä
- Peli ohi viesti

Suurimpana on itse pelin käyttöliittymä, jossa on grafiikka nopille, pisteille ja nappeja noppien heittoon, noppien pitämiseen ja pisteiden saantiin
Pelin käyttöliittymä käyttää Yatzy, Dice, Scores ja UpdateScore luokkia

## Sovelluslogiikka

```mermaid
classDiagram
Score<|--Dice: silmäluku
Yatzy<|--Dice: *
Yatzy<|--Scores: *
Yatzy<|--UpdateScore
    class Yatzy{
    }
    class Scores{
        +summa
        +kombinaatiot
    }
    class Dice{
        +nopan pito
        +silmäluku
        +nopan grafiikka
    }
    class UpdateScore{
        +yläpuolen pisteet
	+alapuolen pisteet
	+kokonaispisteet
    }
