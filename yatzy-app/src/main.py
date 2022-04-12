import tkinter as TK
import random

root=TK.Tk()

rolls_left = TK.IntVar(root)
rolls_left.set(2)

score = TK.IntVar(root)
score.set(0)
scoretext = TK.Label(root, textvariable=score, width=20, height=1)

turns = 0

s_ones = 0
s_twos = 0
s_threes = 0
s_fours = 0
s_fives = 0
s_sixes = 0

s_threeofakind = 0
s_fourofakind = 0
s_fullhouse = 0
s_smallstraight = 0
s_largestraight = 0
s_chance = 0
s_yahtzee = 0

die1 = TK.StringVar(root)
die2 = TK.StringVar(root)
die3 = TK.StringVar(root)
die4 = TK.StringVar(root)
die5 = TK.StringVar(root)

root.configure(bg="#9F561F")
root.geometry("1000x800")
l1=TK.Label(root,font=("Helvetica",175))


class Dice():
    currentdice = []
    def __init__(self):
        self.hold = False
        self.number = None
        Dice.currentdice.append(self)
    
    def holding(self, boolean):
        self.hold = boolean

def new_dice():
    Dice.currentdice = []

def generaterandom():
    numbers = []
    for i in range(1,6):
        numbers.append(random.randrange(1,7)) 
    return numbers

def roll():
    numbers = generaterandom()
    dice = ["z","\u2680","\u2681","\u2682","\u2683","\u2684","\u2685"]
    l1.config(text=f"{dice[numbers[0]]}{dice[numbers[1]]}{dice[numbers[2]]}{dice[numbers[3]]}{dice[numbers[4]]}", bg="#9F561F")
    l1.pack(pady=50)
    bnoppa1.pack(side=TK.LEFT, ipadx=50)
    bnoppa2.pack(side=TK.LEFT, ipadx=50)
    bnoppa3.pack(side=TK.LEFT, ipadx=50)
    bnoppa4.pack(side=TK.LEFT, ipadx=50)
    bnoppa5.pack(side=TK.LEFT, ipadx=50)

def rolls_left():
    left = 3
    return left

def hold(die):
    Dice.holding(die, True)
    
def no_hold(die):
    Dice.holding(die, False)

def update():
    xdice1 = dice.currentdice[0].number
    xdice2 = dice.currentdice[1].number
    xdice3 = dice.currentdice[2].number
    xdice2 = dice.currentdice[3].number
    xdice3 = dice.currentdice[4].number
    
    ones = TK.StringVar(root)
    ones.set("Ykköset")
    twos = TK.StringVar(root)
    twos.set("Kakkoset")
    threes = TK.StringVar(root)
    threes.set("Kolmoset")
    fours = TK.StringVar(root)
    fours.set("Neloset")
    fives = TK.StringVar(root)
    fives.set("Vitoset")
    sixes = TK.StringVar(root)
    sixes.set("Kutoset")
    threeofakind = TK.StringVar(root)
    threeofakind.set("Kolme Samaa Silmälukua")
    fourofakind = TK.StringVar(root)
    fourofakind.set("Neljä Samaa Silmälukua")
    fullhouse = TK.StringVar(root)
    fullhouse.set("Täyskäsi")
    smallstraight = TK.StringVar(root)
    smallstraight.set("Pieni Suora")
    largestraight = TK.StringVar(root)
    largestraight.set("Suuri Suora")
    chance = TK.StringVar(root)
    chance.set("Sattuma")
    yatzy = TK.StringVar(root)
    yatzy.set("Yatzy")

b1=TK.Button(root,text="Heitetään noppaa!", foreground="green",command=roll)
b1.place(x=100,y=0)
b1.pack()

bnoppa1=TK.Button(root,text="Pidä noppa", foreground="green",command=hold(die1))
bnoppa2=TK.Button(root,text="Pidä noppa", foreground="green",command=hold(die2))
bnoppa3=TK.Button(root,text="Pidä noppa", foreground="green",command=hold(die3))
bnoppa4=TK.Button(root,text="Pidä noppa", foreground="green",command=hold(die4))
bnoppa5=TK.Button(root,text="Pidä noppa", foreground="green",command=hold(die5))

remaining_rolls = TK.Label(root, textvariable=rolls_left(), width=50, height=5)
remaining_rolls.pack()

root.mainloop()