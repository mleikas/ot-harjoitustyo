import tkinter as TK

class Dice(TK.Frame, TK.Checkbutton):
    """Luokka, jonka avulla määritetään nopat. 
    
    Tähän kuuluu nopan silmäluvun muuttuja ja pidetäänkö noppaa vai ei
    
    """
    def __init__(self, master):
        """Luokan konstruktori, joka luo uuden nopan
        
        """
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