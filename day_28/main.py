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
timer = None

reps = 0

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_label.grid(column=2, row=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
bg_photo = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=bg_photo)
timer_text = canvas.create_text(103, 130, text="00:00", fill='white', font=(FONT_NAME, 35, 'bold'))
print('timer_text')
print(timer_text)
canvas.grid(column=2, row=2)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(seconds):
    secs = seconds % 60
    mins = seconds // 60
    if secs < 10:
        secs = f'0{secs}'

    if secs == 0:
        secs = "00"
    canvas.itemconfig(timer_text, text=f'{mins}:{secs}')
    if seconds > 0:
        global timer
        timer = window.after(1000, count_down, seconds - 1)
    else:
        on_start()

# ---------------------------- TIMER MECHANISM ------------------------------- #
def on_start():
    print("Start")
    global reps
    global timer
    reps += 1

    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_secs)
        timer_label.config(text='Long break')
    elif reps % 2 == 0:
        count_down(short_break_secs)
        timer_label.config(text='Short break')
    else:
        count_down(work_secs)
        timer_label.config(text='Work time')


start_button = Button(text="Start", command=on_start, bg=YELLOW, highlightthickness=0)
start_button.grid(column=1, row=3)

# ---------------------------- TIMER RESET ------------------------------- #
def on_reset():
    global timer
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    reps = 0
    timer_label.config(text='Timer')
    print("Reset")


reset_button = Button(text="Reset", command=on_reset, bg=YELLOW, highlightthickness=0)
reset_button.grid(column=3, row=3)

check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
check_marks.grid(column=2, row=4)

window.mainloop()
