import sys
import tkinter as tk
from tkinter import ttk, messagebox

class login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Window")
        self.geometry("300x100")
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self._create_widgets()

    def _create_widgets(self):
        # Create the username entry box
        self.username_label = ttk.Label(self, text="Username:")
        self.username_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.username_entry = ttk.Entry(self, textvariable=self.username)
        self.username_entry.grid(row=0, column=1, sticky="w", padx=5, pady=5)
        # Create the password entry box
        self.password_label = ttk.Label(self, text="Password:")
        self.password_label.grid(row=1, column=0, sticky="e")
        self.password_entry = ttk.Entry(self, textvariable=self.password, show="*")
        self.password_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        # Create the login button
        self.login_button = ttk.Button(self, text="Login", command=self._login)
        self.login_button.grid(row=2, column=1, sticky="w", padx=5, pady=5)
    
    def _login(self):
        if self.username.get() == "admin" and self.password.get() == "admin":
            messagebox.showinfo("Login Successful", "Welcome to the system!" + self.username.get())
            self.destroy()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")
            self.username_entry.delete(0, "end")
            self.password_entry.delete(0, "end")


if __name__ == "__main__":
    app = login()
    app.mainloop()
    sys.exit()




# label_username = ttk.Label(window, text="Username:")
# label_username.grid(row=0, column=0, padx=5, pady=5)

# username = ttk.Entry(window, width=20, justify=tk.CENTER)
# username.grid(row=0, column=1, padx=5, pady=5)
# username.insert(0, "Enter your name")
# username.select_range(0, tk.END)
# username.focus()

# label_password = ttk.Label(window, text="Password:")
# label_password.grid(row=1, column=0, padx=5, pady=5)
# password = ttk.Entry(window, width=20, justify=tk.CENTER, show="*")
# password.grid(row=1, column=1, padx=5, pady=5)

# def exit():
#     window.quit()
#     window.destroy()
#     print("Exit")
#     sys.exit()

# def menu():
#     main_menu = Menu(window)
#     file_submenu = Menu(main_menu, tearoff=0)
#     file_submenu.add_separator()
#     file_submenu.add_command(label="Exit", command=exit)
#     help_submenu = Menu(main_menu, tearoff=0)
#     help_submenu.add_command(label="About")
#     main_menu.add_cascade(label="File", menu=file_submenu)
#     main_menu.add_cascade(label="Help", menu=help_submenu)
#     window.config(menu=main_menu)

# menu()

# def login():
#     if password.get() == "":
#         messagebox.showerror("Error", "Please enter your password")
#     else:
#         messagebox.showinfo("Login", "Login Successful\n\nWelcome " + username.get())
        

# send_button = ttk.Button(window, text="Login", command=login)
# send_button.grid(row=2, column=1, padx=5, pady=5)

# window.mainloop()