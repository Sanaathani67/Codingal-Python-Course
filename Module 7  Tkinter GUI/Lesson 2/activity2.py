from tkinter import *

window=Tk()
window.title("Create Account Form")
window.geometry("400x400")

frame=Frame(master=window, height=200, width=360, bg="#d0efff")

lbl1=Label(frame, text="Full Name", bg="#d0efff", fg="white", width=12)
lbl2=Label(frame , text="Email ID", bg="#d0efff", fg="white", width=12)
lbl3=Label(frame, text="Password", bg="#d0efff", fg="white", width=12)

name_entery=Entry(frame)
email_entery=Entry(frame)
pwd_entery=Entry(frame, show="*")

def display():
    name=name_entery.get()
    greeting=f"Hey, {name}!"
    message="\nCongrats on ur new account!"
    textbox.insert(END, greeting)
    textbox.insert(END, message)



textbox=Text(bg="#BEBEBE", fg="black")

btn=Button(text="Create Account", command=display, bg="red")


#arrange all widgets
frame.place(x=20, y=0)

lbl1.place(x=20, y=20)
name_entery.place(x=150, y=20)

lbl2.place(x=20, y=80)
email_entery.place(x=150, y=80)

lbl3.place(x=20, y=140)
pwd_entery.place(x=150, y=140)

btn.place(x=130, y=210)
textbox.place(y=250)

window.mainloop()