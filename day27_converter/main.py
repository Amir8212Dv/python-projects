from tkinter import Tk, Entry, Label, Button

font = ("Arial", 12, "bold")

window = Tk()
window.title("Mile To Km Converter")
window.config(padx=30, pady=15)

miles_input = Entry(width=15)
miles_input.grid(column=2, row=1)

miles_label = Label(text="Miles", pady=10, font=font)
miles_label.grid(column=3, row=1)


is_equal_label = Label(text="is equal to", font=font)
is_equal_label.grid(column=1, row=2)

km_value_label = Label(text="0", padx=50, font=font)
km_value_label.grid(column=2, row=2)

km_label = Label(text="KM", font=font)
km_label.grid(column=3, row=2)


def calculate():
    mile = int(miles_input.get() or "0")
    km = mile * 1.609
    km_value_label.config(text=f"{km}")


calculate_button = Button(
    text="Calculate",
    command=calculate,
    font=font,
)
calculate_button.grid(column=2, row=3)

window.mainloop()
