from tkinter import *  
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "alarm clock"
WORK_MIN = 5
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 3
reps = 0
check = "✔"
time = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(time)
    canvas.itemconfig(timer_text, text="00:00", fill= "white", font=(FONT_NAME, 30, "bold"))
    timer.config(text="Timer", font=("Courier", 50), fg=GREEN, bg=YELLOW, padx=10, pady=10)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, check
    reps+=1
    if reps %8 == 0:
        countdown(int(LONG_BREAK_MIN))
        timer.config(text="BREAK",fg=RED)


    elif reps %2 == 0:
        countdown(int(SHORT_BREAK_MIN))
        timer.config(text="BREAK",fg=PINK)


    else:
        countdown(int(WORK_MIN))
        timer.config(text="WORK",fg=GREEN)
    if reps %2 == 0:
        tick.config(text = check)
        check += "✔"





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
from math import floor
def countdown(count):
    global time
    # print(count)
    count_min = floor(count / 60)
    if count_min<10:
        count_min= f"0{count_min}"

    seconds = count % 60
    if seconds<10:
        seconds= f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{seconds}")

    if count>0:
        time = window.after(1000,countdown, count-1)
    else:
        start_timer()
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg= YELLOW)


canvas  = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file = "tomato.png")
canvas.create_image(100,112, image = tomato)
timer_text=canvas.create_text(100,130, text="00:00", fill= "white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1,column=1)

timer = Label(text="Timer", font=("Courier", 50), fg=GREEN, bg=YELLOW, padx=10, pady=10)
timer.grid(row=0,column=1)

start = Button(text = "Start",command=start_timer)
start.grid(row=2,column=0)

resetter = Button(text="Reset", command=reset)
resetter.grid(row=2,column=2)

tick = Label(text="", font=("Courier"), fg=GREEN, bg=YELLOW)
tick.grid(row=3,column=1)


window.mainloop()
