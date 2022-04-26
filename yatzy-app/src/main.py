import tkinter as TK
import random
import tkinter.messagebox

scorelist = [1, 2, 3, 4, 5, 6, "Kolme samaa", "Neljä samaa", "Full House", "Pieni suora", "Suuri suora", "Yatzy", "Sattuma"]
top_list = [1,2,3,4,5,6]
dice = ["\u2610","\u2680","\u2681","\u2682","\u2683","\u2684","\u2685"]

class Yatzy(TK.Frame):
    def __init__(self, master):
        TK.Frame.__init__(self, master, bg="#9F561F", borderwidth=50)
        self.master = master
        self.scores = {}
        for i in scorelist:
            self.scores[i] = None
        self.dice = []
        for i in range(5):
            self.dice.append(Dice(self))
        self.top_score = 0
        self.bottom_score = 0
        self.temp_scores = {}
        for i in scorelist:
            self.temp_scores[i] = 0
        self.remaining_rolls = 3

        for i, n in enumerate(self.dice):
            n.grid(row=i, column=0, padx=1, pady=1,sticky="E")
            TK.Label(self, font=("Helvetica",30), text="Pidä Noppa").grid(row=i, column=0, padx=1, pady=1,sticky="E")
        self.update_dice_art()
        TK.Button(self,text="Heitetään noppaa!", font=("Helvetica",30), foreground="green",command=self.roll).grid(row=i+1, column=0, rowspan=2)
        row = 0
        col = 1
        self.score_table = []
        for i, j in self.scores.items():
            frame = Scores(self, i, j)
            self.score_table.append(frame)
            frame.grid(row=row, column=col+1,sticky="S", padx=20)
            row += 2
            if row == 6:
                row = 0
                col += 1
        self.updatescore = UpdateScore(self)
        self.updatescore.grid(row=row, column=col+1,sticky="S",pady=10, padx=40)

    def check_scores(self): #Mahdollisesti lisätään pari ja kaksi paria tai sitten pelataan USA:n säännöillä
        for i in scorelist:
            self.temp_scores[i] = 0
        values = []
        for i in self.dice:
            values.append(i.number.get())
        values.sort()
        for i in range(1,7):
            self.temp_scores[i] = sum([x for x in values if x == i])
            if values.count(i) >= 3:
                self.temp_scores["Kolme samaa"] = sum(values)
                if len(set(values)) == 2:
                    self.temp_scores["Full House"] = 19
            if values.count(i) >= 4:
                self.temp_scores["Neljä samaa"] = sum(values)
            if values.count(i) == 5:
                self.temp_scores["Yatzy"] = 50
            str_check = "".join(sorted(list(set([str(a) for a in values]))))
            for i in ["1234","2345","3456"]:
                if i in str_check:
                    self.temp_scores["Pieni suora"] = 15
                    break
            if str_check in ["12345","23456"]:
                self.temp_scores["Suuri suora"] = 20
            self.temp_scores["Sattuma"] = sum(values)
    
    def roll(self):
        if self.remaining_rolls > 0:
            for i in self.dice:
                if i.hold.get() or not i.number.get():
                    i.number.set(random.randrange(1,7))
                self.check_scores()
            self.update_dice_art()
            self.remaining_rolls -= 1
    
    def game_over(self): # Peli ohi vielä työn alla
        if None in self.scores.values():
            top_score = sum([self.scores[i] for i in scorelist[:6]])
            if top_score >= 63:
                bonus = 50
            else:
                bonus = 0
            bottom_score = sum([self.scores[i] for i in scorelist[6:]])
            total = top_score + bonus + bottom_score
            message1 = f"Vasemman puolen pisteet: {top_score}\n Bonus: {bonus}\n Oikean puolen pisteet: {bottom_score}\n Kokonaispisteet: {total}"
            TK.messagebox.showinfo(title="Peli loppui!", message=message1)

    def update_score(self):
        self.updatescore.var_top_score.set(self.top_score)
        self.updatescore.var_bottom_score.set(self.bottom_score)  
        self.updatescore.var_sum_score.set(self.top_score+self.bottom_score)    

    def update_dice_art(self):
        for i, n in enumerate(self.dice):
            self.dice_art = TK.Label(self, text=dice[n.number.get()],textvar=dice[n.number.get()],fg="black",bg="#9F561F",font=("Helvetica",75))
            self.dice_art.grid(row=i, column=1)

    def __call__(self):
        self.pack()
        self.mainloop()

class Dice(TK.Frame, TK.Checkbutton):
    def __init__(self, master):
        self.master = master
        TK.Frame.__init__(self, master)
        self.hold = TK.BooleanVar()
        self.hold.set(True)
        self.number = TK.IntVar()
        self.number.set(0)
        self.off_color = TK.PhotoImage(width=300,height=50)
        self.on_color = TK.PhotoImage(width=300,height=50)
        self.off_color.put(("green",), to=(0,0,80,50))
        self.on_color.put(("red",), to=(0,0,80,50))
        TK.Checkbutton.__init__(self, master=master, font=("Helvetica",30), image=self.off_color, selectimage=self.on_color, var=self.hold) 
        
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

Yatzy(TK.Tk())()