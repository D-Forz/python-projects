import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu

window = tk.Tk()
window.geometry('500x500')
window.title("Menu Component")

label_username = ttk.Label(window, text="Username")
label_username.grid(row=0, column=0)

username = ttk.Entry(window, width=20, justify=tk.CENTER)
username.grid(row=1, column=0)
username.insert(0, "Enter your name")
username.select_range(0, tk.END)
username.focus()

password = ttk.Entry(window, width=20, justify=tk.CENTER, show="*")
password.grid(row=2, column=0)

def exit():
    window.quit()
    window.destroy()
    print("Exit")
    sys.exit()

def menu():
    main_menu = Menu(window)
    file_submenu = Menu(main_menu, tearoff=0)
    file_submenu.add_command(label="Open")
    file_submenu.add_command(label="New")
    file_submenu.add_separator()
    file_submenu.add_command(label="Exit", command=exit)
    help_submenu = Menu(main_menu, tearoff=0)
    help_submenu.add_command(label="About")
    main_menu.add_cascade(label="File", menu=file_submenu)
    main_menu.add_cascade(label="Help", menu=help_submenu)
    window.config(menu=main_menu)

menu()

def send_data():
    
    username.delete(0, tk.END)
    if username.get() == "":
        messagebox.showerror("Error", "Please enter your name")

send_button = ttk.Button(window, text="Send", command=send_data)

window.mainloop()