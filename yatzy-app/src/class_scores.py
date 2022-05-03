"""
Luokka kombinaatiopainikkeille ja niiden antamille pisteille
"""
import tkinter as TK

top_list = [1,2,3,4,5,6]
teksti = ["-","Ykköset","Kakkoset","Kolmoset","Neloset","Viitoset","Kuutoset"]
class Scores(TK.Frame):
    """Luokka, jonka avulla hoidetaan painikkeet pisteiden saantia varten

    Attributes:
        score: Pisteiden määrä
        name: Painikkeen nimi
    """
    def __init__(self, master, name, score=None):
        """Luokan konstruktori, joka luo painikkeen pisteille ja pistemuuttujan,
        joka pitää kirjaa painikkeen pisteistä

        Args:
            score: Pisteiden määrä
            name: Painikkeen nimi
        """
        self.master = master
        TK.Frame.__init__(self, master)
        text = name
        if name in top_list:
            text = teksti[name]
        self.name = name
        self.score = score
        self.var_score = TK.IntVar()
        self.button = TK.Button(self, text=text, command=self.press, font=("Helvetica",15))
        self.button.pack(side="left")
        self.label = TK.Label(self, textvar=self.var_score)
        self.label.pack(side="left")

    def press(self):
        """Painikketta painaessa tallentaa saadut pisteet ja muuttaa painikkeen väriä

        Lisäksi, jos kaikki painikkeet ovat painettu, peli loppuu

        """
        if self.score is None and 0 not in [i.number.get() for i in self.master.dice]:
            self.master.scores[self.name] = self.master.temp_scores[self.name]
            self.score = self.master.temp_scores[self.name]
            self.var_score.set(self.score)
            for i in self.master.dice:
                i.number.set(0)
                i.hold.set(True)
            if self.name in top_list:
                self.master.top_score += self.score
            else:
                self.master.bottom_score += self.score
            self.button.config(bg="green")
            self.label.config(bg="green")
            self.master.update_score()
            self.master.remaining_rolls = 3

            if None not in self.master.scores.values():
                self.master.game_over()
