from tkinter import *
import winsound

# ---------------------------- CONSTANTS ------------------------------- #
BROWN = "#83764F"
BEIGE = "#A2A378"
LIGHT_GREEN = "#E5F9DB"
GREEN = "#A0D8B3"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
checkmarks_update = ""
countdown_timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    print("reset timer")
    title_update = "Timer"
    title_label.config(text=title_update)
    window.after_cancel(countdown_timer)
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps-=1 #come back to the previous session


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    
    if (reps % 2) == 1: # work 
        countdown_update(WORK_MIN*60)
        title_update = "Work"
    elif (reps == 6): # 6o ciclo é a pausa longa
        countdown_update(LONG_BREAK_MIN*60)
        title_update = "Break"
        reps=0
    else: # breaks
        countdown_update(SHORT_BREAK_MIN*60)
        title_update = "Break"
        
    title_label.config(text=title_update)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown_update(count):
    global countdown_timer
    # break the time in min and sec
    minutes = int(count / 60)
    seconds = int(count - (minutes * 60))
    time_update = f"{minutes:02}:{seconds:02}"
    
    canvas.itemconfig(timer_text, text=time_update)
    if count > 0:
        countdown_timer = window.after(1000, countdown_update, count-1)
    else:
        # Play a system alert sound
        global checkmarks_update
        if (reps % 2) == 1: # work 
            checkmarks_update=checkmarks_update+"🌱" # ✓ 🌱 🍃
            check_marks.config(text=checkmarks_update)
        winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomototoro")
window.geometry("620x740")
window.config(padx=20, pady=20, bg=LIGHT_GREEN)

title_label = Label(window, text="Timer", font=(FONT_NAME, 48, "bold"), bg=LIGHT_GREEN, fg=BROWN)
title_label.grid(row=0, column=0, columnspan=3)

#* canvas
canvas = Canvas(width=600, height=700, bg=LIGHT_GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="totoro.png")
canvas.create_image(300, 460, image=tomato_img)
# timer
timer_text = canvas.create_text(300, 520, text="00:00", fill=BROWN, font=(FONT_NAME,40, "bold"))

canvas.grid(row=2, column=0, columnspan=3)

#* Counter
check_marks = Label(text="", fg=GREEN, bg=LIGHT_GREEN, font=(FONT_NAME, 32, "bold"))
check_marks.grid(row=1, column=1)

#* BUTTONS
#start button
button_start = Button(text="Start", command=start_timer, font=(FONT_NAME, 20, "bold"), fg=BROWN, bg=GREEN)
button_start.grid(row=1, column=0)

#reset button
button_reset = Button(text="Reset", command=reset_timer, font=(FONT_NAME, 20, "bold"), fg=BROWN, bg=GREEN)
button_reset.grid(row=1, column=2)

window.mainloop()