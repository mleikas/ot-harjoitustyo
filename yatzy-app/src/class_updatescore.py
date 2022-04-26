import tkinter as TK
import random

class UpdateScore(TK.Frame):
    def __init__(self, master):
        self.master = master
        TK.Frame.__init__(self, master)
        self.var_top_score = TK.IntVar()
        self.var_top_score.set(self.master.top_score)
        self.var_bottom_score = TK.IntVar()
        self.var_bottom_score.set(self.master.bottom_score)
        self.var_bonus = TK.IntVar()
        self.var_bonus.set(0)
        self.var_sum_score = TK.IntVar()
        self.var_sum_score.set(self.master.top_score+self.master.bottom_score+self.var_bonus.get())
        TK.Label(self, text="Vasemman puolen pisteet").pack(side="top")
        TK.Label(self, textvar=self.var_top_score).pack(side="top")
        TK.Label(self, text="Oikean puolen pisteet").pack(side="top")
        TK.Label(self, textvar=self.var_bottom_score).pack(side="top")
        TK.Label(self, text="Kokonaispisteet").pack(side="top")
        TK.Label(self, textvar=self.var_sum_score).pack(side="top")
