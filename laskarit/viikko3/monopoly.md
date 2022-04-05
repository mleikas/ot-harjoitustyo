## Monopoli sovelluslogiikka

```mermaid
classDiagram
Pelaaja<|--Noppa: heitot
Pelaaja<|--Ruutu: käynti
	class Pelaaja{
        +maara
        +pelinappula
        +lokaatio
        +vuoro
	}
	class Noppa{
        +heitto
    }
    class Ruutu{
        +ruuduntyyppi
    }

```
