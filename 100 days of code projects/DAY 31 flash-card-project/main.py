#*****************************************IMPORTS AND CONSTANTS*****************************************#
from tkinter import *
import random
BACKGROUND_COLOR = "#B1DDC6"
#****************************************DATA READING******************************************#
import pandas as pd
data= pd.read_csv("data/french_words.csv")
translations = data.to_dict(orient="records")
current_card = {}

#**************************************RIGHT BUTTON********************************************#
def is_known():
    translations.remove(current_card)
    data = pd.DataFrame(translations)
    data.to_csv('data/unknown.csv')
    generate_word()
#**************************************WRONG BUTTON********************************************#
def generate_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(translations)
    canvas.itemconfig(word, text = current_card['French'],fill="black")
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(flip_image, image=front)
    flip_timer = window.after(3000, func= flip_card)


#**************************************Flip the card********************************************#
def flip_card():
    canvas.itemconfig(title, text = "English", fill="white")
    canvas.itemconfig(word, text = current_card['English'], fill="white")
    canvas.itemconfig(flip_image, image=back)
#**************************************Flip the card End********************************************#
#**********************************UI SETUP************************************************#
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flash App")

flip_timer = window.after(3000, func= flip_card)

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR, highlightthickness=0)

front = PhotoImage(file = "images/card_front.png")
back = PhotoImage(file = "images/card_back.png")
flip_image =canvas.create_image(400,263,image = front)
title = canvas.create_text(400,130, text='Title',font=("Times New Roman", 40, "italic"))
word = canvas.create_text(400,260,text = "word", font =(("Times New Roman", 50, "bold")) )

canvas.grid(row=0,column=0,columnspan=2)

wrong = PhotoImage(file="images/wrong.png")
unknown_button= Button(image=wrong,highlightthickness=0, command=generate_word)
unknown_button.grid(row=1,column=1)

right = PhotoImage(file="images/right.png")
known_button=Button(image=right,highlightthickness=0,command=is_known)
known_button.grid(row=1,column=0)

generate_word()
window.mainloop()