from tkinter import *
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open("data.txt", mode="a") as data:
        data.write(f"{website.get()} | {email.get()} | {password.get()}\n")
        website.delete(0, END)
        password.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200,height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image = lock_img)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

website = Entry(width=50)
website.focus()
website.grid(column=1,row=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)

email = Entry(width=50)
email.insert(0,"bresh@gmail.com")
email.grid(column=1,row=2,columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

password = Entry(width= 31)
password.grid(column=1, row=3)

# generate_password = Button(text="Generate Password", width=15)
# generate_password.grid(column=2,row=3)

add_password = Button(text="Add", width=43,command=save)
add_password.grid(column=1,row=4,columnspan=2)








window.mainloop()