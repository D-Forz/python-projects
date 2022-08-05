import tkinter
from tkinter import ttk

window = tkinter.Tk()

# config window size, title and icon.
window.geometry('500x500')
window.title("My Window")
window.iconbitmap('Learning_projects\Tkinter\grid_manager\icon.ico')

# Configure rows and columns
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=5)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=5)

def event():
    button_one.config(text="Button Clicked")
    # ttk.Button(window, text="New Button").pack()

def event4():
    button_four.config(text="Button Clicked", fg="red", relief="raised")

    # lambda: print("Clicked")

# create a button and bind it to the event function.
button_one = ttk.Button(window, text="Click Me", command=event)
button_one.grid(row=0, column=0, sticky="NSWE", padx=10, pady=10, columnspan=2)

button_two = ttk.Button(window, text="Click Me")
button_two.grid(row=0, column=1, sticky="NSWE")

button_three = ttk.Button(window, text="Click Me")
button_three.grid(row=1, column=0, sticky="NSWE")

# create a button with tkinter and bind it to the event4 function.
button_four = tkinter.Button(window, text="Click Me", command=event4)
button_four.grid(row=1, column=1, sticky="NSWE")

window.mainloop()