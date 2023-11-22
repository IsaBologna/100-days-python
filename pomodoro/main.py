from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
BROWN = "#83764F"
BEIGE = "#A2A378"
LIGHT_GREEN = "#E5F9DB"
GREEN = "#A0D8B3"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    print("reset timer")
    # countdown_update(0)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    
    if (reps % 2) == 1: # work 
        countdown_update(WORK_MIN*60)
        title_update = "Timer"
    elif (reps == 6): # 6o ciclo é a pausa longa
        countdown_update(LONG_BREAK_MIN*60)
        title_update = "Long Break"
        reps=0
    else: # breaks
        countdown_update(SHORT_BREAK_MIN*60)
        title_update = "Short Break"
        
    title_label.config(text=title_update)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown_update(count):
    minutes = int(count / 60)
    seconds = count - (minutes * 60)
    time_update = f"{minutes:02}:{seconds:02}"
    canvas.itemconfig(timer_text, text=time_update)
    if count > 0:
        window.after(1000, countdown_update, count-1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomototoro")
window.geometry("620x740")
window.config(padx=20, pady=20, bg=LIGHT_GREEN)

title_label = Label(window, text="Timer", font=(FONT_NAME, 48, "bold"), bg=LIGHT_GREEN, fg=BROWN)
title_label.grid(row=0, column=1)

#* canvas
canvas = Canvas(width=600, height=850, bg=LIGHT_GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="totoro.png")
canvas.create_image(300, 460, image=tomato_img)
# timer
timer_text = canvas.create_text(300, 520, text="00:00", fill=BROWN, font=(FONT_NAME,40, "bold"))
#Counter
canvas.create_text(300, 100, text="✓", fill=GREEN, font=(FONT_NAME, 48, "bold"))
canvas.grid(row=2, column=0, columnspan=3)

#* BUTTONS
#start button
button_start = Button(text="Start", command=start_timer, font=(FONT_NAME, 20, "bold"), fg=BROWN, bg=GREEN)
button_start.grid(row=1, column=0)

#reset button
button_reset = Button(text="Reset", command=reset_timer, font=(FONT_NAME, 20, "bold"), fg=BROWN, bg=GREEN)
button_reset.grid(row=1, column=2)

window.mainloop()