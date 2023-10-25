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

current_cycles = 4

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

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


def count_down(seconds):
    if seconds >= 0:
        text = str(seconds // 60) + ":" + (str(seconds % 60) if seconds % 60 > 0 else "00")
        canvas.itemconfig(timer_text, text=f'{str(seconds // 60)}:{(str(seconds % 60) if seconds % 60 > 0 else "00")}')
        window.after(1000, count_down, seconds - 1)


def on_start():
    print("Start")
    current_cycles = 4
    count_down(WORK_MIN * 60)


start_button = Button(text="Start", command=on_start, bg=YELLOW, highlightthickness=0)
start_button.grid(column=1, row=3)

def on_reset():
    print("Reset")


def update_timer(mins, secs):
    return

reset_button = Button(text="Reset", command=on_reset, bg=YELLOW, highlightthickness=0)
reset_button.grid(column=3, row=3)

check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
check_marks.grid(column=2, row=4)

window.mainloop()
