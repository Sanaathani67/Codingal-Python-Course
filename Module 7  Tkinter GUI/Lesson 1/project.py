from tkinter import *
from datetime import datetime

window = Tk()

window.title("This is my first Tkinter app")
window.geometry("600x400")

lbl = Label(text="HELLO!", fg="#90EE90", bg="#663399", height=2, width=600, font=(None, 25))

name_lbl = Label(text="Full Name", bg="#3895D3")

name_entry = Entry()

def display():
    name = name_entry.get()
    greeting = f"What's up, {name}?\n"
    message = "Welcome to my world!\nToday's date is: "
    text_block.delete("1.0", "end")
    text_block.insert(END, greeting)
    text_block.insert(END, message)
    text_block.insert(END, datetime.now())

def homework():
    text_block.delete("1.0", "end")
    text_block.insert(END, "Did you do your HW?")

btn = Button(text="Begin", command=display, height=1, bg="#1261A0", fg="white")

hw_btn = Button(text="Did you do your HW?", command=homework, height=1, bg="#1261A0", fg="white")

text_block = Text(height=3)

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
hw_btn.pack()
text_block.pack()

window.mainloop()