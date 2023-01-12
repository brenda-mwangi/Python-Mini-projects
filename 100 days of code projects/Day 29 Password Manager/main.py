from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]+[random.choice(symbols) for char in range(nr_symbols)]+[random.choice(numbers) for char in range(nr_numbers)]
    random.shuffle(password_list)

    password = "".join(password_list)
    if len(password_entry.get()) >0:
        password_entry.delete(0, END)
        if len(password_entry.get()) <=0:
            password_entry.insert(0, password)
    else:
        password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website.get()
    em = email.get()
    pw = password_entry.get()
    if len(pw) >0 and len(em)>0 and len(web)>0:
    
        is_ok=messagebox.askokcancel(title=web, message=f"These are the details entered:\nEmail:{em}\nPassword: {pw}\nIs it okay to save?")
        
        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"{web} | {em} | {pw}\n")
                website.delete(0, END)
                password_entry.delete(0, END)
    else:
        messagebox.showinfo(title=web,message="Don't leave empty spaces")

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

password_entry = Entry(width= 31)
password_entry.grid(column=1, row=3)

generate_password = Button(text="Generate Password", width=15, command=generate)
generate_password.grid(column=2,row=3)

add_password = Button(text="Add", width=43,command=save)
add_password.grid(column=1,row=4,columnspan=2)



window.mainloop()