from tkinter import *
from tkinter import ttk
root=Tk()

b1=ttk.Button(root,text='click me')
b1.pack()

def buCick(x):
   print("clicked{}".format(x))
b1.config(command= lambda : buCick(1))

root.mainloop()


