
import tkinter as tk 
from tkinter import *


root = tk.Tk()
root.title("Toplevel Example")

def toplevel(): 
	top = Toplevel()
	top.title("Toplevel")
	label = tk.Label(top, text = "this is a toplevel :)")
	label.pack()
	top.mainloop()

button = tk.Button(root, text = "open toplevel", command = toplevel)
button.pack()

root.mainloop()