from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# Function selected
def selected(event):
    for i in range(0, len(p_name)):
        if clicked.get() == p_name[i]:
            myLabel = Label(root, text = xlsname[i]).pack()
            break



# Width X Height
root.geometry("1920x1080")

# Displaying the Image
photo = PhotoImage(file = "cricket-stats.png")
label1 = Label(image = photo)
label1.pack()


#width, height
root.minsize(300, 100)
root.maxsize(1200, 988)

"""
myLabel = Label(text = "This is a Label")
myLabel.pack()
"""
