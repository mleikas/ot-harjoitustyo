import tkinter as TK
import random

top_list = [1,2,3,4,5,6]

class Scores(TK.Frame):
    def __init__(self, master, name, score=None):
        self.master = master
        TK.Frame.__init__(self, master)
        text = name
        if name == 1:
            text = "Ykköset"
        if name == 2:
            text = "Kakkoset"
        if name == 3:
            text = "Kolmoset"
        if name == 4:
            text = "Neloset"
        if name == 5:
            text = "Viitoset"
        if name == 6:
            text = "Kuutoset"
        self.name = name
        self.score = score
        self.var_score = TK.IntVar()
        self.button = TK.Button(self, text=text, command=self.press, font=("Helvetica",15))
        self.button.pack(side="left")
        self.label = TK.Label(self, textvar=self.var_score)
        self.label.pack(side="left")
    
    def press(self):
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

            if None in self.master.scores.values():
                pass
            else:
                self.master.game_over()
