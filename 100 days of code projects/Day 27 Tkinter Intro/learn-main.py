import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# label
label = tkinter.Label(text="Me Label", font=("Arial", 24))
label.pack(expand=True)

label1 = tkinter.Label(text="Me Label2", font=("Arial", 24, "italic"))
label1.pack(side="left")

label2 = tkinter.Label(text="Me Label3", font=("Arial", 24, "bold"))
label2.pack()

window.mainloop()
