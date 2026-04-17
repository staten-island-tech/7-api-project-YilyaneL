# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("GOATED API PROJECTOS")
# Set geometry (widthxheight)
root.geometry('1080x700')

lbl = Label(root, text = "R U POOPY BUTT MCHCIKEN")
lbl.grid(column = 0, row = 0)

txt = Entry(root, width=30)
txt.grid(column=0,row=2)

def clicked():
    lbl.configure(text = "i just got clicked", fg="red")

btn = Button(root, text = "click me kid", fg = 'blue', command=clicked)
btn.grid(column=0,row=1)

root.mainloop()