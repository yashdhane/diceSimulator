#im so excited really!!!!

from tkinter import *
import random

root = Tk()
root.geometry("720x450")

l1 = Label(root,font= ("Times",200) )

def roll():
    number=['\u2680', '\u2861', '\u2682', '\u2683', '\u2684', '\u2685']
    l1.config(text=f'{random.choice(number)}{random.choice(number)}')
    l1.pack()

b1 = Button(root,text="roll", width=4, height=4, command=roll)
b1.place(x=350,y=0)

root.mainloop()

