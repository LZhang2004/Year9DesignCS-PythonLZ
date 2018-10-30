#main game
#http://jjal.download/index.php?module=sms&lang=en - Phone Notification Fake all going to use this for the messages
import tkinter as tk 
from tkinter import *
from PIL import ImageTk, Image
import math 
import os 
import time

root = tk.Tk()
root.title("Game")

#enable and disable keypad and message buttons
def enableMessage(): 
	messagebutton.config(state = "normal")

def enableKeypad(): 
	keypadbutton.config(state = "normal")

def useless():
	storyline.insert(tk.INSERT, "")

username = "username"





#The text box for the story (Begin)
def StoryBegin():
	storyline.config(state = "normal")
	storyline.insert(tk.INSERT, "\nSecretCipher : By Leo Zhang")
	storyline.insert(tk.INSERT,"\nVersion 1.0.4")
	storyline.insert(tk.INSERT,"\nEntering....")
	storyline.insert(tk.INSERT,"\nThis is the tutorial!!!")
	storyline.insert(tk.INSERT,"\nYou are in the enemy base")
	storyline.insert(tk.INSERT,"\nYou need to get into the office...")
	storyline.insert(tk.INSERT,"\nThere is a number lock on the door...")
	storyline.insert(tk.INSERT,"\nYou got a message on your phone!...")
	storyline.insert(tk.INSERT,"\nPress Recieve Message when done reading this!")
	root.after(1000, enableMessage) 
	storyline.config(state = "disabled")

#The tutorial box - just a gray frame
def display_tutorial_password(): 
	top = Toplevel(visual = "truecolor")
	top.title("PhoneMessage") #http://jjal.download/index.php?module=sms&lang=en
	top.configure(background='grey')

#The function to destroy the username thing, show photo, and disable username box and enable input password, set command for the messages button to #2
	def please(): 
		n = str(entr.get())
		path = "/Users/"+n+"/Desktop/SecretCipher/Images/tutorial_password.png"
		img = ImageTk.PhotoImage(Image.open(path))
		panel = tk.Label(top, image = img)
		panel.grid(column = 0, row = 0)
		btn1.destroy()
		title.destroy()
		entr.destroy()
		title2.destroy()
		message = tk.Label(top, text = "After you have read this, click the red button in the top left corner", fg = "black", font = ("Courier", 20) )
		message.grid(column = 0, row = 1)
		message2 = tk.Label(top, text = "and you can now click the <enter password> button on the right of the window", fg = "black", font = ("Courier", 20) )
		message2.grid(column = 0, row = 2)
		username = n;
		messagebutton.config(state = "disabled", command = Choice1)
		messagebutton.config(text = "CHOICE")
		keypadbutton.config(state = "normal")
		top.mainloop()
	# the input username box - so all computers can use
	title = tk.Label(top, text = "Please input your computer username for this to work (example - leo.zhang)", fg = "black", font = ("Courier", 20) )
	title.grid(column = 0, row = 0)
	title2 = tk.Label(top, text = "If nothing happens, the username is incorrect", fg = "black", font = ("Courier", 20) )
	title2.grid(column = 0, row = 1)
	btn1 = tk.Button(top, text = "Submit", command = please, font = ("Arial", 20, "bold"), fg = 'red')
	btn1.config(height = 3, width = 10)
	btn1.grid(column = 0, row = 4)
	entr = tk.Entry(top)
	entr.grid(column = 0, row = 3)
	n = str(entr.get())
	username = n;
	
#keypad frame for tutorial input	
def keypad1(): 
	top = Toplevel()
	top.title("keypad1")
	#function to check the input
	def check(): 
		n = int(entr.get())

		#function to close keypad, refresh storyline text, enable level 1, turn begin to green
		def please2():
				top.destroy()
				messagebutton.config(state = "disabled")
				keypadbutton.config(state = "disabled")
				beginbutton.config(fg = 'green', command = useless)
				level1button.config(state = "normal")
				storyline.config(state = "normal")
				storyline.delete('1.0', END)
				storyline.insert(tk.INSERT, "Congrats on completing the tutorial!!!")
				storyline.insert(tk.INSERT, "\nClick Level 1 to continue :)")
				storyline.config(state = "disabled")
				top.mainloop()
		#continuing the check if answer is right
		if n == 9832:
			title3.config(text = "Status: CORRECT! Wait 3 seconds for continue", fg = "green")
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







def LevelOne(): 
	storyline.config(state = "normal")
	storyline.delete('1.0', END)
	storyline.insert(tk.INSERT,"\nCongrats on completing the tutorial btw :) ")
	storyline.insert(tk.INSERT,"\nNow, you're in the building")
	storyline.insert(tk.INSERT,"\nWhat do you do now?")
	storyline.insert(tk.INSERT,"\nClick on the CHOICE button to continue")
	root.after(1000, enableMessage) 
	storyline.config(state = "disabled")	



def Choice1(): 
	def Upstairs():
		choice1.destroy()
		messagebutton.config(text = "Recieve Message")
		keypadbutton.config(command = keypad2a)
		messagebutton.config(state = "disabled")
		keypadbutton.config(state = "normal")
		storyline.config(state = "normal")
		storyline.delete('1.0', END)
		storyline.insert(tk.INSERT,"\nYou decide to walk UPSTAIRS")
		storyline.insert(tk.INSERT,"\nThere is a Lock on the Door!")
		storyline.insert(tk.INSERT,"\nThere is a paper taped beside the keypad")
		storyline.insert(tk.INSERT,"\nIt says {The password is 12 in base 3 }")	
		storyline.insert(tk.INSERT,"\nYou need to convert the number 12 into Base 3 for the password")	
		storyline.insert(tk.INSERT,"\nWhen you are ready, press the input")
		storyline.insert(tk.INSERT,"\npassword button!")
		storyline.config(state = "disabled")
		
	choice1 = Toplevel(visual = "")
	choice1.title("Choice1") #http://jjal.download/index.php?module=sms&lang=en
	choice1.configure(background='grey')
	btn1 = tk.Button(choice1, text = "Lets go upstairs", command = Upstairs, font = ("Arial", 20, "bold"), fg = 'red')
	btn1.grid(column = 0, row = 0)
	btn2 = tk.Button(choice1, text = "Lets go downstairs", command = Downstairs, font = ("Arial", 20, "bold"), fg = 'red')
	btn2.grid(column = 1, row = 0)
	choice1.mainloop()



def keypad2a():
	lock = Toplevel()
	lock.title("Lock")
	locknumber1 = 0
	label2 = 0
	label3 = 0

	def left1():
		locknumber1 == int(locknumber1)
		if locknumber1 >= 1:
			locknumber1 == locknumber1 - 1
		elif locknumber1 == 0:
			locknumber1 == 10
		else:
			print("error")
		Label1.config(text = str(locknumber1))

	def right1():
		locknumber1 == int(locknumber1)
		if locknumber1 <= 9:
			locknumber1 == locknumber1 + 1
		elif locknumber1 == 10:
			locknumber1 == 0
		else:
			print("error")
		Label1.config(text = str(locknumber1))

	def left2():
		label2 == int(label2)
		if label2 >= 1:
			label2 == label2 - 1
		else:
			label2 == 10
		Label2.config(text = label2)

	def right2():
		label2 == int(label2)
		if label2 <= 9:
			label2 == label2 + 1
		else:
			label2 == 0
		Label2.config(text = label2)


	left1 = tk.Button(lock, text = "<<<<-----", command = left1)
	left1.grid(column = 0, row = 0)
	right1 = tk.Button(lock, text = "----->>>>", command = right1)
	right1.grid(column = 3, row = 0)
	Label1 = tk.Label(lock, text = str(locknumber1))
	Label1.grid(column = 2, row = 0)
	left2 = tk.Button(lock, text = "<<<<-----", command = left2)
	left2.grid(column = 0, row = 1)
	right2 = tk.Button(lock, text = "----->>>>", command = right2)
	right2.grid(column = 3, row = 1)
	Label2 = tk.Label(lock, text = str(label2))
	Label2.grid(column = 2, row = 1)

	lock.mainloop()








def Downstairs():
	choice1.destroy()
	storyline.config(state = "normal")
	storyline.insert(tk.INSERT,"\nCongrats on completing the tutorial btw :) ")
	storyline.insert(tk.INSERT,"\nNow, you're in the building")
	storyline.insert(tk.INSERT,"\nWhat do you do now?")
	storyline.insert(tk.INSERT,"\nClick on the CHOICE button to continue")




def LevelTwo(): 
	storyline.config(state = "normal")


def LevelThree(): 
	storyline.config(state = "normal")

def LevelFour(): 
	storyline.config(state = "normal")

def LevelFive(): 
	storyline.config(state = "normal")










#Title Label
title = tk.Label(root, text = "Welcome to the Game", fg = "black", font = ("Courier", 44) )
title.grid(column = 2, row = 0)

#Begin
beginbutton = tk.Button(root, text = "Begin", command = StoryBegin, font = ("Arial", 20, "bold"), fg = 'red')
beginbutton.config(height = 3, width = 10)
beginbutton.grid(column = 2, row = 1)

#Level buttons
level1button = tk.Button(root, text = "Level 1", font = ("Arial", 20, "bold"), command = LevelOne, state = "disabled", fg = 'red')
level1button.config(height = 3, width = 10)
level1button.grid(column = 0, row = 2)

btn3 = tk.Button(root, text = "Level 2", command = LevelTwo, font = ("Arial", 20, "bold"), fg = 'red', state = "disabled")
btn3.config(height = 3, width = 10)
btn3.grid(column = 1, row = 2)

btn4 = tk.Button(root, text = "Level 3", command = LevelThree, font = ("Arial", 20, "bold"), fg = 'red', state = "disabled")
btn4.config(height = 3, width = 10)
btn4.grid(column = 2, row = 2)

btn5 = tk.Button(root, text = "Level 4", command = LevelFour, font = ("Arial", 20, "bold"), fg = 'red', state = "disabled")
btn5.config(height = 3, width = 10)
btn5.grid(column = 3, row = 2)

btn6 = tk.Button(root, text = "Level 5", command = LevelFive, font = ("Arial", 20, "bold"), fg = 'red', state = "disabled")
btn6.config(height = 3, width = 10)
btn6.grid(column = 4, row = 2)

#text box
storyline = tk.Text(root, width = 50, height = 10, borderwidth = 3, relief = tk.GROOVE)
storyline.config(state = "disabled")
storyline.grid(column = 2, row = 3)

#display message button and display keypad button
messagebutton = tk.Button(root, text = "Recieve Message", command = display_tutorial_password, font = ("Arial", 20, "bold"), fg = 'green', state = "disabled")
messagebutton.config(height = 3, width = 20)
messagebutton.grid(column = 2, row = 5)

keypadbutton = tk.Button(root, text = "Enter Password", command = keypad1, font = ("Arial", 20, "bold"), fg = 'green', state = "disabled")
keypadbutton.config(height = 3, width = 20)
keypadbutton.grid(column = 3, row = 3)


root.mainloop()