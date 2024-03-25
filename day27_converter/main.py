from tkinter import Tk, Entry, Label, Button

font = ("Arial", 12, "bold")

window = Tk()
window.title("Mile To Km Converter")
window.config(padx=30, pady=15)

input = Entry(width=15)
input.grid(column=2, row=1)

miles_label = Label(text="Miles", pady=10, font=font)
miles_label.grid(column=3, row=1)


desc_1 = Label(text="is equal to", font=font)
desc_1.grid(column=1, row=2)

converted_value_label = Label(text="0", padx=50, font=font)
converted_value_label.grid(column=2, row=2)

measure_name = Label(text="KM", font=font)
measure_name.grid(column=3, row=2)


def calculate():
    mile = int(input.get() or "0")
    km = mile * 1.609
    converted_value_label.config(text=f"{km}")


calculate_button = Button(
    text="Calculate",
    command=calculate,
    font=font,
)
calculate_button.grid(column=2, row=3)

window.mainloop()
