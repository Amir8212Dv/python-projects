import tkinter
import time

YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
RED = "#e7305b"
PINK = "#e2979c"
FONT_NAME = "Courier"
CHECK_MARK = "✔️"

w = tkinter.Tk()
w.config(bg=YELLOW)
w.minsize(width=700, height=700)
w.title("Pomodoro")

status_label = tkinter.Label(text="Timer", font=(FONT_NAME, 60), bg=YELLOW, fg=GREEN)
status_label.place(x=250, y=50)

canvas = tkinter.Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer = canvas.create_text(100, 112, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.place(x=250, y=200)


complete_work_sessions_label = tkinter.Label(
    text="Completed Sessions: 0", fg=GREEN, bg=YELLOW, font=("Arial", 10, "bold")
)
complete_work_sessions_label.place(x=275, y=500)

work_time = 0
break_time = 0
completed_work_sessions = 0


def start():
    global timer, work_time, break_time, completed_work_sessions
    work_time = 60 * 25 * 0.01
    break_time = 60 * 5 * 0.01

    status_label.config(text="Work")
    while work_time > 0:
        m = str(int(work_time // 60))
        m = f"0{m}" if len(m) == 1 else m
        s = str(int(work_time % 60))
        s = f"0{s}" if len(s) == 1 else s
        canvas.delete(timer)
        timer = canvas.create_text(100, 112, text=f"{m}:{s}", fill="white", font=(FONT_NAME, 25, "bold"))
        w.update()
        time.sleep(1)
        work_time -= 1

    if break_time:
        status_label.config(text="Break")
    while break_time >= 0:
        m = str(int(break_time // 60))
        m = f"0{m}" if len(m) == 1 else m
        s = str(int(break_time % 60))
        s = f"0{s}" if len(s) == 1 else s
        canvas.delete(timer)
        timer = canvas.create_text(100, 112, text=f"{m}:{s}", fill="white", font=(FONT_NAME, 25, "bold"))
        w.update()
        time.sleep(1)
        break_time -= 1
        if break_time == 0:
            completed_work_sessions += 1
            complete_work_sessions_label.config(text=f"Completed Sessions: {completed_work_sessions}")
            start()


def reset():
    global timer, work_time, break_time
    work_time = 0
    break_time = 0
    status_label.config(text="Timer")
    canvas.delete(timer)
    timer = canvas.create_text(100, 112, text=f"00:00", fill="white", font=(FONT_NAME, 25, "bold"))
    w.update()


start_button = tkinter.Button(text="start", command=start, bg="white", border=0, width=10, font=("Arial", 12))
start_button.place(x=150, y=500)

reset_button = tkinter.Button(text="reset", command=reset, bg="white", border=0, width=10, font=("Arial", 12))
reset_button.place(x=450, y=500)


w.mainloop()
