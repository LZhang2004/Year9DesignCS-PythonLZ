import tkinter as tk


def null():
	print("")

root = tk.Tk() 

#FUNCTIONSSS
def ok():
	print("hey")


def Encrypt():
	print("E")

def Decrypt():
	print("D")



title = tk.Label(root, text = "Welcome to Encryptor", fg = "black", font = ("Courier", 44) )
title.grid(column = 1, row = 0)


# DROP DOWN MENU
var = tk.StringVar(root)
var.set("Nothing") # initial value
option = tk.OptionMenu(root, var, "Caesar Cipher", "two", "three", "four")
option.grid(column = 2, row = 1)


# RADIO BUTTONSSS
MODES = [
("Encrypt", "1"),
("Decrypt", "2"),
]
v = tk.StringVar()
v.set("1")

for r in range(0,len(MODES),1):
	b = tk.Radiobutton(root, text=MODES[r][0], variable = v, value=MODES[r][0], command = ok)
	b.grid(column = 0, row = r+1)


#input box
inputbox = tk.Text(root)
inputbox.config(width = 50, height = 10, relief = tk.GROOVE, borderwidth = 3)
inputbox.grid(column = 0, row = 3)

#MIDDLE BUTTON
mainbutton = tk.Button(root, text = "Encrypt", command = check)
mainbutton.grid(column = 1, row = 3)

#output box 
outputbox = tk.Text(root)
outputbox.config(width = 50, height = 10, relief = tk.GROOVE, borderwidth = 3)
outputbox.grid(column = 2, row = 3)










root.mainloop()
