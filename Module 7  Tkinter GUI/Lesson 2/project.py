from tkinter import *

window = Tk()
window.title("ATM PIN Setup Interface")
window.geometry("400x500")

details_frame = Frame(window, width=350, height=120, bg="#D9EAF7")

account_label = Label(details_frame, text="Account Name", bg="#D9EAF7")
account_entry = Entry(details_frame)

pin_label = Label(details_frame, text="PIN", bg="#D9EAF7")
pin_entry = Entry(details_frame, show="*")

def confirm_pin():
    account = account_entry.get()
    pin = pin_entry.get()
    
    message_box.delete("1.0", END)
    
    if account and pin:
        message_box.insert(END, "ATM PIN set successfully!")
    else:
        message_box.insert(END, "Please enter your account name and PIN.")

keypad_frame = Frame(window, relief=SUNKEN, borderwidth=2)

keypad_values = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
    ["*", "0", "#"]
]

for row in range(4):
    for column in range(3):
        cell = Frame(keypad_frame, relief=RAISED, borderwidth=1)
        cell.grid(row=row, column=column, padx=3, pady=3)
        
        button = Button(cell, text=keypad_values[row][column], width=5, height=2)
        button.pack()

confirm_button = Button(
    window,
    text="Set ATM PIN",
    command=confirm_pin,
    bg="#1261A0",
    fg="white"
)

message_box = Text(window, width=35, height=4)

details_frame.place(x=25, y=20)

account_label.place(x=15, y=15)
account_entry.place(x=120, y=15)

pin_label.place(x=15, y=55)
pin_entry.place(x=120, y=55)

keypad_frame.place(x=75, y=160)

confirm_button.place(x=135, y=370)

message_box.place(x=35, y=415)

window.mainloop()