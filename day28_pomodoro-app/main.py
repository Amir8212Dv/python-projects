import tkinter
from PIL import ImageTk, Image
import time

w = tkinter.Tk()
w.minsize(width=700, height=700)

timer_label = tkinter.Label(text="Timer", font=("Arial", 60))
timer_label.place(x=250, y=50)

timer = tkinter.Label(text="00:00", font=("Arial", 30, "bold"))
timer.place(x=100, y=100)

tomato = ImageTk.PhotoImage(Image.open("tomato.png"))
l = tkinter.Label(text="00:00", image=tomato, fg="white")
l.place(x=250, y=200)


def start():
    for i in range(60 * 25, 0, -1):
        m = str(i // 60)
        m = f"0{m}" if len(m) == 1 else m
        s = str(i % 60)
        s = f"0{s}" if len(s) == 1 else s
        print(m, " : ", s)
        timer_label.config(text=f"{m}:{s}")
        time.sleep(1)


start_button = tkinter.Button(text="start", command=start)
start_button.place(x=150, y=500)

reset_button = tkinter.Button(text="reset")
reset_button.place(x=500, y=500)


w.mainloop()
