from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk


root = Tk()
root.geometry("400x400")

# Drop down boxes

# To show the selection
def selected(event):
    myLabel = Label(root, text = clicked.get()).pack()
    for i in range(0, len(options)):
        if clicked.get() == options[i]:
            myLabel = Label(root, text = sname[i]).pack()
            break

def comboclick(event):
    myLabel = Label(root, text = myCombo.get()).pack()
    for i in range(0, len(options)):
        if myCombo.get() == options[i]:
            myLabel = Label(root, text = sname[i]).pack()
            break        

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
