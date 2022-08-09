import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfile

class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Text Editor")
        self.rowconfigure(0, minsize=600, weight=1)
        self.columnconfigure(1, minsize=600, weight=1)
        self.text = tk.Text(self, wrap=tk.WORD)
        self.file = None
        self.file_open = False
        self.create_components()
        self.create_menu()

    def create_components(self):
        frame_buttons = tk.Frame(self, relief=tk.RAISED, bd=2)
        button_open = tk.Button(frame_buttons, text="Open", command=self._open_file)
        button_save = tk.Button(frame_buttons, text="Save", command=self._save_file)
        button_save_as = tk.Button(frame_buttons, text="Save as...", command=self._save_file_as)
        button_save_as.grid(row=0, column=0, sticky="we", padx=5, pady=5)
        button_open.grid(row=1, column=0, sticky="we", padx=5, pady=5)
        button_save.grid(row=2, column=0, sticky="we", padx=5, pady=5)
        frame_buttons.grid(row=0, column=0, sticky="ns")
        self.text.grid(row=0, column=1, sticky="nswe")

    def create_menu(self):
        menu_app = tk.Menu(self)
        self.config(menu=menu_app)
        menu_file = tk.Menu(menu_app, tearoff=False)
        menu_app.add_cascade(label="File", menu=menu_file)
        menu_file.add_command(label="Open", command=self._open_file)
        menu_file.add_command(label="Save", command=self._save_file)
        menu_file.add_command(label="Save as...", command=self._save_file_as)
        menu_file.add_separator()
        menu_file.add_command(label="Exit", command=self.quit)
        menu_help = tk.Menu(menu_app, tearoff=False)
        menu_app.add_cascade(label="Help", menu=menu_help)
        menu_help.add_command(label="About", command=self._about)

    def _open_file(self):
        self.file = askopenfile(mode="r", filetypes=[("Text files", "*.txt")])
        if self.file:
            self.text.delete(1.0, tk.END)
            self.text.insert(1.0, self.file.read())
            self.file_open = True
            self.title(self.file.name)
    
    def _save_file(self):
        if self.file_open:
            self.file.close()
            self.file = open(self.file.name, "w")
            self.file.write(self.text.get(1.0, tk.END))
            self.file.close()
        else:
            self._save_file_as()
    
    def _save_file_as(self):
        self.file = asksaveasfile(mode="w", filetypes=[("Text files", "*.txt")])
        if self.file:
            self.file.write(self.text.get(1.0, tk.END))
            self.file.close()
            self.file_open = True
            self.title(self.file.name)

    def _about(self):
        tk.messagebox.showinfo("About", "Text Editor")

if __name__ == "__main__":
    app = Editor()
    app.mainloop()