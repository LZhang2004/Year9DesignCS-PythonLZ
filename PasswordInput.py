import tkinter as tk 


top = tk.Tk()
top.title("keypad1")
#function to check the input
def check(): 
	n = int(entr.get())
	#function to close keypad, refresh storyline text, enable level 1, turn begin to green
	#continuing the check if answer is right
	if n == 9832:
		title3.config(text = "Status: CORRECT! ", fg = "green")
		top.after(2000, please2)
		
	else: 
		title3.config(text = "Status: INCORRECT! Please Try Again", fg = "red")
#frame for the keypad 
title2 = tk.Label(top, text = "Enter the Password", fg = "black", font = ("Courier", 20) )
title2.grid(column = 0, row = 0)
entr = tk.Entry(top)
entr.grid(column = 0, row = 1)
btn1 = tk.Button(top, text = "Submit", command = check, font = ("Arial", 20, "bold"), fg = 'red')
btn1.config(height = 3, width = 10)
btn1.grid(column = 0, row = 2)
title3 = tk.Label(top, text = "Status: Password not entered", fg = "black", font = ("Courier", 30) )
title3.grid(column = 0, row = 3)
top.mainloop()
