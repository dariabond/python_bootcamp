from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(height=500, width=300)

label = Label(text="My label", font=("Aerial", 24, "italic"))
label['text'] = "New label"
label.config(text="Again new text")
label.grid(column=1, row=1)

def button_clicked():
    print('Clicked!')
    label['text'] = input.get()

new_button = Button(text="New button", command=button_clicked)
new_button.grid(column=3, row=1)

button = Button(text="My button", command=button_clicked)
button.grid(column=2, row=2)

input = Entry(width=10)
input.grid(column=4, row=4)

window.mainloop()
