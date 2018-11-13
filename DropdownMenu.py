import tkinter as tk


def change(*args):
	print("running change")
	print(var.get())

root = tk.Tk() 

title = tk.Label(root, text = "Welcome to Encryptor", fg = "black", font = ("Courier", 44) )
title.grid(column = 1, row = 0)

OPTIONS = [
	"Caesar Cipher",
	"bunny",
	"chicken",
]
var = tk.StringVar(root)
var.set(OPTIONS[0])
var.trace("w",change)
dropDownMenu = tk.OptionMenu(root,var, OPTIONS[0],OPTIONS[1],OPTIONS[2])
dropDownMenu.grid(column = 2, row = 1)


MODES = [
("Encrypt", "1"),
("Decrypt", "2"),
]
v = tk.StringVar() 
v.set("1")

for r in range(0,len(MODES),1):
	b = tk.Radiobutton(root, text=MODES[r][0], variable = v, value=MODES[r][0], command = change)
	b.grid(column = 0, row = r+1)


root.mainloop()
