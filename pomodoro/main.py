from tkinter import *

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

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def button_clicked():
    print("Button clicked")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomototoro")
window.config(padx=50, pady=20, bg=LIGHT_GREEN)

# canvas
canvas = Canvas(width=600, height=850, bg=LIGHT_GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="totoro.png")
canvas.create_image(300, 460, image=tomato_img)
# timer
canvas.create_text(300, 580, text="00:00", fill=BROWN, font=(FONT_NAME,40, "bold"))
#start button
button_start = Button(text="Start", command=button_clicked)
button_start.grid()
#Counter
canvas.create_text(300, 100, text="v", fill=GREEN, font=(FONT_NAME, 48, "bold"))
#reset button
button_reset = Button(text="Stop", command=button_clicked)
button_reset.grid()

canvas.grid()

window.mainloop()