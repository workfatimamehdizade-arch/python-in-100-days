from tkinter import *
import math
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
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label1.config(text="Timer", fg=GREEN, bg=YELLOW)
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(work_sec)
        label1.config(text="Working", fg=GREEN, bg=YELLOW)
    elif reps == 2 or reps == 4 or reps == 6:
        count_down(short_break_sec)
        label1.config(text="Break", fg=PINK, bg=YELLOW)

    elif reps == 8:
        count_down(long_break_sec)
        label1.config(text="Long Break", fg=PINK, bg=YELLOW)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count /60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)

tomato_img = PhotoImage(file="tomato.png")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(103,130,text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2,row=2)

label1 = Label(text="Timer", fg=GREEN,bg=YELLOW, font=(FONT_NAME, 35))
label1.grid(column=2,row=1)
check_marks = Label(fg=GREEN,bg=YELLOW, font=(FONT_NAME, 35))
check_marks.grid(column=2,row=4)

button1 = Button(text="Start", bg=YELLOW, highlightthickness=0, borderwidth=0, relief="flat", command=start_timer)
button2 = Button(text="Reset", bg=YELLOW, highlightthickness=0, borderwidth=0, relief="flat", command=reset_timer)
button2.grid(column=3,row=3)
button1.grid(column=1,row=3)


window.mainloop()

