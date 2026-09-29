from tkinter import *
from tkinter import messagebox 
import random

root=Tk()
root.geometry("200x200")

def msg():
    messagebox.showerror("Alert", "Stop! VIRUS FOUND !")

button=Button(root, text="Scan for virus", command=msg)
button.place(x=40, y=80)

def change_color():
    hexcode=random.randint(0, 0xFFFFFF)
    hexcode_string=f"#{hexcode:06x}"#only 6 characters
    root.config(bg=hexcode_string)
    
button2=Button(root, text="My colourful Life!", command=change_color)
button2.place(x=60, y=140)


root.mainloop()