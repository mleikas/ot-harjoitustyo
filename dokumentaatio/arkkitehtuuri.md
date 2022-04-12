## Sovelluslogiikka

```mermaid
classDiagram
Score<|--Dice: silmäluku

    class Score{
        +summa
        +kombinaatiot
    }
	class Dice{
        +heitto
        +silmäluku
    }