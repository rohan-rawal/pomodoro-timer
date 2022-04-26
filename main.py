from ctypes.wintypes import SHORT
from itertools import count
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):

    minute = count // 60
    second = count % 60
    
    if second < 10:
        second = "0" + str(second)
    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        window.after(1000, countdown, count-1)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


label1 = Label(text="Timer", font=(FONT_NAME, 28, "bold"), fg=GREEN, bg=YELLOW)
label1.grid(column=1, row=0)

label2 = Label(text="✔", fg=GREEN, bg=YELLOW)
label2.grid(column=1, row=3)

button1 = Button(text="Start", highlightthickness=0, command=start_timer)
button1.grid(column=0, row=2)

button2 = Button(text="Reset", highlightthickness=0)
button2.grid(column=2, row=2)

window.mainloop()