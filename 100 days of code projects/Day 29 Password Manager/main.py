from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
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
    new_data = {
            web:{
                "email": em,
                "password": pw,
            },
        }
    if len(pw) >0 and len(em)>0 and len(web)>0:
        with open("data.json", mode="r") as data:
            try:
                existing_data = json.load(data)
        # update data
                existing_data.update(new_data)
            except:
                with open("data.json", mode="w") as data:
                    json.dump(new_data,data, indent=4)

            else:
                with open("data.json", mode="w") as data:
                # save updated data
                    json.dump(existing_data,data, indent=4)
            finally:
                website.delete(0, END)
                password_entry.delete(0, END)
            messagebox.showinfo(title=web, message="Password added successfully")

    else:
        messagebox.showinfo(title=web,message="Don't leave empty spaces")
# ---------------------------- SEARCH PASSWORDS ------------------------------- #
def search_password():
    check_website = website.get()
    if len(check_website)>0:
        with open("data.json", "r") as file:
            try:
                cd = json.load(file)
                messagebox.showinfo(title = check_website, message = f"Email: {cd[check_website]['email']}\nPassword: {cd[check_website]['password']}")
                pyperclip.copy(cd[check_website]['password'])

            except KeyError:
                messagebox.showerror(title = check_website, message = f"No Data Found")
    else:
        messagebox.showerror(title = check_website, message = f"Website Empty!")
                  


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200,height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image = lock_img)
canvas.grid(column=1,row=0)

website_label = Label(text="Website: ")
website_label.grid(column=0,row=1)

website = Entry(width=31)
website.focus()
website.grid(column=1,row=1)

search_button = Button(text="Search", padx=25, command=search_password)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)

email = Entry(width=49)
email.insert(0,"bresh@gmail.com")
email.grid(column=1,row=2,columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

password_entry = Entry(width= 31)
password_entry.grid(column=1, row=3)

generate_password = Button(text="Generate Password", width=14, command=generate)
generate_password.grid(column=2,row=3)

add_password = Button(text="Add", width=41,command=save)
add_password.grid(column=1,row=4,columnspan=2)



window.mainloop()