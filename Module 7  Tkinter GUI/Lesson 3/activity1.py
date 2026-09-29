#import neccessary libraries
from tkinter import *

#create window
window=Tk()
window.title("Event handler")
window.geometry("100x100")

#event handler for keypress
def handle_keypress(event):
    """Print the character associated to the key pressed(docstring)"""
    print(event.char)

#Bind keypress event  to handle_keypress
window.bind("<Key>", handle_keypress)

#Event handler foe button click
def handle_click(event):
    print("\nThe button was clicked!")

button=Button(text="Click me!")
button.pack()

#Bind click event to handle_click()
button.bind("<Button-3>", handle_click)

#start GUI
window.mainloop()