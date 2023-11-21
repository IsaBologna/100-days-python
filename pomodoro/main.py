from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
BROWN = "#83764F"
BEIGE = "#A2A378"
LIGHT_GREEN = "#E5F9DB"
GREEN = "#A0D8B3"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    print("Button clicked")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown_update():
    pass

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
canvas.create_text(300, 520, text="00:00", fill=BROWN, font=(FONT_NAME,40, "bold"))
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