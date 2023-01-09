from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20) #padding all round the screen

def got_click():
    label1.config(text=input.get())
    print("Button Got Clicked")
# label

# label["text"] = "My label"
# label.config(text="New text2")
label1 = Label(text="Me Label2", font=("Arial", 24, "italic"))
# label1.place(x=100,y=50)
label1.grid(column=0,row=0)
label1.config(padx=20,pady=20)
# label2 = tkinter.Label(text="Me Label3", font=("Arial", 24, "bold"))
# label2.pack()

# Button
def got_click():
    label1.config(text=input.get())
    # print("Button Got Clicked")

button = Button(text="Click Me", command=got_click)
# button.pack()
button.grid(column=1,row=1)

button2 = Button(text="New button")
button2.grid(column=2, row=0)
# Entry or input
input = Entry(width=30)
input.grid(column=3,row=2)


window.mainloop()
