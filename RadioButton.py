import tkinter as tk

def change():
	print("change")
	print(v.get()) #Accesses element associated with MODES

root = tk.Tk()

MODES = [
("Monochrome", "1"),
("Grayscale", "L"),
("True color", "RGB"),
("Color separation", "CMYK"),
]
v = tk.StringVar() 
v.set("L")

for r in range(0,len(MODES),1):
	b = tk.Radiobutton(root, text=MODES[r][0], variable=v, value=MODES[r][1], command = change)
	b.pack(anchor=tk.W)


root.mainloop()