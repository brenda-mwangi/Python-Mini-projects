from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flash App")

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
front = PhotoImage(file = "images/card_front.png")
# back = PhotoImage(file = "images/card_back.png")
canvas.create_image(400,263,image = front)
canvas.create_text(400,100,text="Title", font=("Times New Roman", 40, "italic"))
canvas.create_text(400,200,text = "word", font =(("Times New Roman", 60, "bold")) )
canvas.grid(row=0,column=0,columnspan=2)

wrong = PhotoImage(file="images/wrong.png")
unknown_button= Button(image=wrong,highlightthickness=0)
unknown_button.grid(row=1,column=1)

right = PhotoImage(file="images/right.png")
known_button=Button(image=right,highlightthickness=0)
known_button.grid(row=1,column=0)



window.mainloop()