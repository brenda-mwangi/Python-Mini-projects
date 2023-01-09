from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500,height=300)
window.config(padx=30, pady=70)

def convert():
    mile_to_km = round((float(input.get()) * 1.609), 1)
    output.config(text = mile_to_km)

equivalent = Label(text="is equivalent to", font=("Times New Roman", 16, "bold"))
equivalent.grid(column=0,row=100)
equivalent.config(padx=30,pady=20)

output = Label(text="0", font=("Times New Roman", 16, "bold"))
output.grid(column=100,row=100)
output.config(padx=20,pady=10)

km = Label(text="Km", font=("Times New Roman", 16, "bold"))
km.grid(column=300,row=100)
km.config(padx=20,pady=10)

input = Entry()
input.grid(column=100,row=0)
input.config(width=10)

mile = Label(text="Miles", font=("Times New Roman", 16, "bold"))
mile.grid(column=300,row=0)
mile.config(padx=20,pady=10)

button = Button(text="Calculate", font=("Times New Roman", 12),command=convert)
button.grid(row=200, column=100)

window.mainloop()