from tkinter import Label, Button, Canvas, Tk, PhotoImage
import time

YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
RED = "#e7305b"
PINK = "#e2979c"
FONT_NAME = "Courier"
CHECK_MARK = "✔️"

w = Tk()
w.config(bg=YELLOW)
w.minsize(width=700, height=700)
w.title("Pomodoro")

status_label = Label(text="Timer", font=(FONT_NAME, 60), bg=YELLOW, fg=GREEN)
status_label.place(x=250, y=50)

canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(100, 112, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.place(x=250, y=200)


complete_work_sessions_label = Label(text="Completed Sessions: 0", fg=GREEN, bg=YELLOW, font=("Arial", 10, "bold"))
complete_work_sessions_label.place(x=275, y=500)

work_time = 0
break_time = 0
completed_work_sessions = 0


def update_timer_label(time: int):
    global timer_text

    m = str(int(time // 60))
    m = f"0{m}" if len(m) == 1 else m
    s = str(int(time % 60))
    s = f"0{s}" if len(s) == 1 else s
    canvas.delete(timer_text)
    timer_text = canvas.create_text(100, 112, text=f"{m}:{s}", fill="white", font=(FONT_NAME, 25, "bold"))
    w.update()


def start_session_countdown():
    global work_time, break_time, completed_work_sessions
    work_time = 60 * 25
    break_time = 60 * 5

    status_label.config(text="Work")
    while work_time > 0:
        update_timer_label(work_time)
        time.sleep(1)
        work_time -= 1

    if break_time:
        status_label.config(text="Break")
    while break_time >= 0:
        update_timer_label(break_time)
        time.sleep(1)
        break_time -= 1
        if break_time == 0:
            completed_work_sessions += 1
            complete_work_sessions_label.config(text=f"Completed Sessions: {completed_work_sessions}")
            start_session_countdown()


def reset_session_countdown():
    global timer, work_time, break_time
    work_time = 0
    break_time = 0
    status_label.config(text="Timer")
    canvas.delete(timer)
    timer = canvas.create_text(100, 112, text=f"00:00", fill="white", font=(FONT_NAME, 25, "bold"))
    w.update()


start_button = Button(text="start", command=start_session_countdown, bg="white", border=0, width=10, font=("Arial", 12))
start_button.place(x=150, y=500)

reset_button = Button(text="reset", command=reset_session_countdown, bg="white", border=0, width=10, font=("Arial", 12))
reset_button.place(x=450, y=500)


w.mainloop()
