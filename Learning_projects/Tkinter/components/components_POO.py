import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class WindowComponents(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Window Components")
        self.geometry("500x500")
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self._create_tabs()
    
    def _entry_component(self, tab):
        entry = ttk.Entry(tab, width=20)
        entry.grid(row=0, column=0, padx=5, pady=5)
        entry.insert(0, "Enter your name")
        entry.select_range(0, tk.END)
        entry.focus()
        label = ttk.Label(tab, text="Hello World!")
        label.grid(row=1, column=0, padx=5, pady=5)
        button = ttk.Button(tab, text="Click Me")
        button.grid(row=2, column=0, padx=5, pady=5)

    def _scrolltext_component(self, tab):
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n"
        scroll = scrolledtext.ScrolledText(tab, width=40, height=10, wrap=tk.WORD)
        scroll.insert(tk.INSERT, text)
        scroll.grid(row=0, column=0, padx=5, pady=5)

    def _combobox_component(self, tab):
        data = [x + 1 for x in range(10)]
        combobox = ttk.Combobox(tab, width=15, values=data)
        combobox.grid(row=0, column=0, padx=5, pady=5)
        combobox.current(0)
        button = ttk.Button(tab, text="Click Me", command=lambda: messagebox.showinfo("value", combobox.get()))
        button.grid(row=1, column=0, padx=5, pady=5)

    def _images_component(self, tab):
        image = tk.PhotoImage(file="tree.png")
        button = ttk.Button(tab, image=image, command=lambda: messagebox.showinfo("Image", image.cget("file")))
        button.grid(row=1, column=0, padx=5, pady=5)

    def _progressbar_component(self, tab):
        progressbar = ttk.Progressbar(tab, orient=tk.HORIZONTAL, length=200, mode='determinate')
        progressbar.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
        progressbar.start()
        button = ttk.Button(tab, text="progress x 10", command=lambda: progressbar.step(10))
        button.grid(row=1, column=0, padx=5, pady=5)
        button_stop = ttk.Button(tab, text="Cancel", command=lambda: progressbar.stop())
        button_stop.grid(row=1, column=1, padx=5, pady=5)

    def _create_tabs(self):
        tabControl = ttk.Notebook(self)
        tab_entry = ttk.Frame(tabControl)
        tabControl.add(tab_entry, text='Tab 1')
        tab_scrolltext = ttk.LabelFrame(tabControl, text="Content")
        tabControl.add(tab_scrolltext, text='Tab 2')
        tab_combobox = ttk.Frame(tabControl)
        tabControl.add(tab_combobox, text='Tab 3')
        tab_images = ttk.LabelFrame(tabControl, text="Images")
        tabControl.add(tab_images, text='Tab 4')
        tab_progressbar = ttk.LabelFrame(tabControl, text="Progressbar") 
        tabControl.add(tab_progressbar, text='Tab 5')
        tabControl.pack(expand=1, fill='both')
        self._entry_component(tab_entry)
        self._scrolltext_component(tab_scrolltext)
        self._combobox_component(tab_combobox)
        self._images_component(tab_images)
        self._progressbar_component(tab_progressbar)
        return tabControl


if __name__ == "__main__":
    window = WindowComponents()
    window.mainloop()