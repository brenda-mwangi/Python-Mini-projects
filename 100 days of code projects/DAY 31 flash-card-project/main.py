#*****************************************IMPORTS AND CONSTANTS*****************************************#
from tkinter import *
from random import randint
BACKGROUND_COLOR = "#B1DDC6"
#****************************************DATA READING******************************************#
import pandas as pd
data= pd.read_csv("data/french_words.csv")
translations = data.to_dict()
#**************************************WRONG AND RIGHT BUTTON********************************************#
def generate_word():
    pairs = {
        'French': {0: 'partie', 1: 'histoire', 2: 'chercher', 3: 'seulement', 4: 'police', 5: 'pensais', 6: 'aide', 7: 'demande', 8: 'genre', 9: 'mois', 10: 'frère', 11: 'laisser', 12: 'car', 13: 'mettre', 14: 'aucun', 15: 'laisse', 16: 'eux', 17: 'ville', 18: 'chaque', 19: 'parlé', 20: 'arrivé', 21: 'devrait', 22: 'bébé', 23: 'longtemps', 24: 'heures', 25: 'vont', 26: 'pendant', 27: 'revoir', 28: 'aucune', 29: 'place', 30: 'parle', 31: 'compris', 32: 'savais', 33: 'étaient', 34: 'attention', 35: 'voici', 36: 'pourrais', 37: 'affaire', 38: 'donner', 39: 'type', 40: 'leurs', 41: 'donné', 42: 'train', 43: 'corps', 44: 'endroit', 45: 'yeux', 46: 'façon', 47: 'écoute', 48: 'dont', 49: 'trouve', 50: 'premier', 51: 'perdu', 52: 'main', 53: 'première', 54: 'côté', 55: 'pouvoir', 56: 'vieux', 57: 'sois', 58: 'tiens', 59: 'matin', 60: 'tellement', 61: 'enfant', 62: 'point', 63: 'venu', 64: 'suite', 65: 'pardon', 66: 'venez', 67: 'devant', 68: 'vers', 69: 'minutes', 70: 'demandé', 71: 'chambre', 72: 'mis', 73: 'belle', 74: 'droit', 75: 'aimerais', 76: "aujourd'hui", 77: 'mari', 78: 'cause', 79: 'enfin', 80: 'espère', 81: 'eau', 82: 'attendez', 83: 'parti', 84: 'nouvelle', 85: 'boulot', 86: 'arrêter', 87: 'dirait', 88: 'terre', 89: 'compte', 90: 'donne', 91: 'loin', 92: 'fin', 93: 'croire', 94: 'chérie', 95: 'gros', 96: 'plutôt', 97: 'aura', 98: 'filles', 99: 'jouer', 100: 'bureau'}, 
        'English': {0: 'part', 1: 'history', 2: 'search', 3: 'only', 4: 'police', 5: 'thought', 6: 'help', 7: 'request', 8: 'kind', 9: 'month', 10: 'brother', 11: 'let', 12: 'because', 13: 'to put', 14: 'no', 15: 'leash', 16: 'them', 17: 'city', 18: 'each', 19: 'speak', 20: 'come', 21: 'should', 22: 'baby', 23: 'long time', 24: 'hours', 25: 'will', 26: 'while', 27: 'meet again', 28: 'any', 29: 'square', 30: 'speak', 31: 'understood', 32: 'knew', 33: 'were', 34: 'Warning', 35: 'here is', 36: 'could', 37: 'case', 38: 'give', 39: 'type', 40: 'their', 41: 'given', 42: 'train', 43: 'body', 44: 'place', 45: 'eyes', 46: 'way', 47: 'listen', 48: 'whose', 49: 'find', 50: 'first', 51: 'lost', 52: 'hand', 53: 'first', 54: 'side', 55: 'power', 56: 'old', 57: 'be', 58: 'here', 59: 'morning', 60: 'so much', 61: 'child', 62: 'point', 63: 'came', 64: 'after', 65: 'sorry', 66: 'come', 67: 'in front of', 68: 'towards', 69: 'minutes', 70: 'request', 71: 'bedroom', 72: 'placed', 73: 'beautiful', 74: 'law', 75: 'would like to', 76: 'today', 77: 'husband', 78: 'cause', 79: 'finally', 80: 'hope', 81: 'water', 82: 'Wait', 83: 'left', 84: 'new', 85: 'job', 86: 'Stop', 87: 'would say', 88: 'Earth', 89: 'account', 90: 'given', 91: 'far', 92: 'end', 93: 'believe', 94: 'sweetheart', 95: 'large', 96: 'rather', 97: 'will have', 98: 'girls', 99: 'to play', 100: 'office'}
    }
    rand = randint(0,100)
    french_word = pairs['French'][rand]
    english_word = pairs['English'][rand]
    canvas.itemconfig(french, text = french_word)
    # canvas.itemconfig(english, text= english_word)

#**********************************UI SETUP************************************************#
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flash App")

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
front = PhotoImage(file = "images/card_front.png")
# back = PhotoImage(file = "images/card_back.png")
canvas.create_image(400,263,image = front)
# canvas.create_image(400,263,image = back)

title = canvas.create_text(400, 100, text='French',font=("Times New Roman", 40, "italic"))

random_index = randint(0,100)
french = canvas.create_text(400,200,text = translations['French'][random_index], font =(("Times New Roman", 50, "bold")) )
# english = canvas.create_text(400,230,text = translations['English'][random_index], font =(("Times New Roman", 30, "bold")) )
canvas.grid(row=0,column=0,columnspan=2)

wrong = PhotoImage(file="images/wrong.png")
unknown_button= Button(image=wrong,highlightthickness=0, command=generate_word)
unknown_button.grid(row=1,column=1)

right = PhotoImage(file="images/right.png")
known_button=Button(image=right,highlightthickness=0,command=generate_word)
known_button.grid(row=1,column=0)

window.mainloop()