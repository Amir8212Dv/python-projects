import tkinter
import time

YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
RED = "#e7305b"
PINK = "#e2979c"
FONT_NAME = "Courier"


w = tkinter.Tk()
w.config(bg=YELLOW)
w.minsize(width=700, height=700)
w.title("Pomodoro")

timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 60))
timer_label.place(x=250, y=50)

canvas = tkinter.Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer = canvas.create_text(100, 112, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.place(x=250, y=200)

remain_time = 0


def start():
    global timer, remain_time
    remain_time = 60 * 25

    while remain_time > 0:
        m = str(remain_time // 60)
        m = f"0{m}" if len(m) == 1 else m
        s = str(remain_time % 60)
        s = f"0{s}" if len(s) == 1 else s
        canvas.delete(timer)
        timer = canvas.create_text(100, 112, text=f"{m}:{s}", fill="white", font=(FONT_NAME, 25, "bold"))
        w.update()
        time.sleep(1)
        remain_time -= 1


def reset():
    global timer, remain_time
    remain_time = 0
    canvas.delete(timer)
    timer = canvas.create_text(100, 112, text=f"00:00", fill="white", font=(FONT_NAME, 25, "bold"))
    w.update()


start_button = tkinter.Button(text="start", command=start)
start_button.place(x=150, y=500)

reset_button = tkinter.Button(text="reset", command=reset)
reset_button.place(x=500, y=500)


w.mainloop()
