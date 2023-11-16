import tkinter as tk

def button_clicked():
    print("Button clicked")
    msg = input.get()
    my_label.config(text=msg)


window = tk.Tk() # create the window
#* window information
window.title("My Program")
window.minsize(width=500, height=300)

#* window elements
# Label
my_label = tk.Label(text="A Label", font=("Arial", 24, "bold"))
my_label.pack(side="top") # geometry management mechanism
# modify a parameter
my_label["text"] = "New Label"
# my_label.config(font=("Arial", 30, "bold"))
# Button
button = tk.Button(text="Submit", command=button_clicked)
button.pack()
# Entry
input = tk.Entry(width=15)
input.pack()

window.mainloop() # run the window, listening to new user inputs
