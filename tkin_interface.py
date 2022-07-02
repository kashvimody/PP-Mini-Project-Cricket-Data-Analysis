from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk


root = Tk()
root.title("My dropdown menu")
root.iconbitmap(r"C:\Users\zaida\Downloads\Cover .PNG")
root.geometry("400x400")

# Drop down boxes
















options = [
    "MS",
    "Virat",
    "Shikhar",
    "Rohit"
]

sname = [
    "Dhoni",
    "Kohli",
    "Dhawan",
    "Sharma"
]

clicked = StringVar()

# Default value
clicked.set("Select a Player")

drop = OptionMenu(root, clicked, *options, command = selected)
drop.pack()

#Combo Box
myCombo = ttk.Combobox(root, value = options)
myCombo.current(0)
myCombo.bind("<<ComboBoxSelected>>", comboclick)
myCombo.pack()

# Get the selection
#myButton = Button(root, text = "Show Selection", command = show).pack()

root.mainloop()
