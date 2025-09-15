import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#379b46"
GREEN_LIGHT = "#9bdeac"
YELLOW = "#F7F5DD"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 50
reps = 0
tempo = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    if tempo:
        window.after_cancel(tempo)
    canvas.itemconfig(timer, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Focus", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = count // 60
    seconds = count % 60

    canvas.itemconfig(timer, text=f"{minutes:02}:{seconds:02}")
    if count > 0:
        global tempo
        tempo = window.after(1000, count_down, count - 1)
    else:
        window.bell() # Toca o som de alerta do sistema
        start_timer()
        marks = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)
        

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Tomate")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = tk.Label(text="Pomodoro", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomate = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomate)  # Placeholder for image
timer = canvas.create_text(102, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", highlightthickness=0, bg=GREEN_LIGHT, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", highlightthickness=0, bg=GREEN_LIGHT, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = tk.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
check_marks.grid(column=1, row=3)









window.mainloop()
