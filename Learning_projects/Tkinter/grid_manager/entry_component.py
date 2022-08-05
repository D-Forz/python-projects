import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
window.geometry('500x500')
window.title("Entry Component")

username = ttk.Entry(window, width=20, justify=tk.CENTER)
username.grid(row=0, column=0)
username.insert(0, "Enter your name")
username.select_range(0, tk.END)
username.focus()

password = ttk.Entry(window, width=20, justify=tk.CENTER, show="*")
password.grid(row=1, column=0)

disabled = ttk.Entry(window, width=20, justify=tk.CENTER, state=tk.DISABLED)
disabled.grid(row=2, column=0)

read_only = ttk.Entry(window, width=20, justify=tk.CENTER)
read_only.grid(row=3, column=0)
read_only.insert(0, "This is read only")
read_only.insert(tk.END, ".")
read_only.config(state='readonly')

def send_data():
    print(username.get())
    print(password.get())
    send_button.config(text=username.get())
    username.delete(0, tk.END)

send_button = ttk.Button(window, text="Send", command=send_data)
send_button.grid(row=0, column=1, rowspan=2, sticky=tk.NSEW)


label_username = ttk.Label(window, text="Username")
label_username.grid(row=4, column=0)
my_var = tk.StringVar(value="Enter your name")
n_username = ttk.Entry(window, width=20, justify=tk.CENTER, textvariable=my_var)
n_username.grid(row=5, column=0)

def send_data2():
    send_button2.config(text=my_var.get())
    my_var.set("Success")
    messagebox.showinfo("This is a info message", my_var.get())
    # messagebox.showerror("This is a error message", my_var.get())
    # messagebox.showwarning("This is a warning message", my_var.get())

send_button2 = ttk.Button(window, text="Send", command=send_data2)
send_button2.grid(row=5, column=1)




window.mainloop()