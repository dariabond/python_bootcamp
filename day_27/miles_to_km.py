from tkinter import *

window = Tk()
window.title("Miles to km converter")
window.minsize(height=130, width=300)

equal_to_label = Label(text="Is equal to", font=("Aerial", 24, "italic"))
equal_to_label.grid(column=1, row=2)

input = Entry(width=10)
input.grid(column=2, row=1)

km_result_label = Label(text="0", font=("Aerial", 24, "italic"))
km_result_label.grid(column=2, row=2)

def button_clicked():
    km_result_label['text'] = int(input.get()) * 1.6

calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=2, row=3)

km_label = Label(text="Miles", font=("Aerial", 24, "italic"))
km_label.grid(column=3, row=1)

miles_label = Label(text="Km", font=("Aerial", 24, "italic"))
miles_label.grid(column=3, row=2)

window.mainloop()
