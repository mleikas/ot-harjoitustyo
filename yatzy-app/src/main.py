from tkinter import *
import random

root=Tk()
root.geometry("1000x500")
l1=Label(root,font=("Helvetica",150))

def generaterandom():
    numbers = []
    for i in range(0,5):
        numbers.append(random.randrange(1,7)) 
    return numbers
   
def roll():
    numbers = generaterandom()
    dice = ["z","\u2680","\u2681","\u2682","\u2683","\u2684","\u2685"]
    l1.config(text=f"{dice[numbers[0]]}{dice[numbers[1]]}{dice[numbers[2]]}{dice[numbers[3]]}{dice[numbers[4]]}")
    l1.pack()

b1=Button(root,text="Heitetään noppaa!", foreground="green",command=roll)
b1.place(x=100,y=0)
b1.pack()

root.mainloop()