import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

window = tk.Tk()
window.geometry('500x500')
window.title("Components")

def entry_component(tab):
    entry = ttk.Entry(tab, width=20)
    entry.grid(row=0, column=0, padx=5, pady=5)
    entry.insert(0, "Enter your name")
    entry.select_range(0, tk.END)
    entry.focus()
    label = ttk.Label(tab, text="Hello World!")
    label.grid(row=1, column=0, padx=5, pady=5)
    button = ttk.Button(tab, text="Click Me")
    button.grid(row=2, column=0, padx=5, pady=5)

def scrolltext_component(tab):
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n"
    scroll = scrolledtext.ScrolledText(tab, width=40, height=10, wrap=tk.WORD)
    scroll.insert(tk.INSERT, text)
    scroll.grid(row=0, column=0, padx=5, pady=5)

def combobox_component(tab):
    data = [x + 1 for x in range(10)]
    combobox = ttk.Combobox(tab, width=15, values=data)
    combobox.grid(row=0, column=0, padx=5, pady=5)
    combobox.current(0)
    button = ttk.Button(tab, text="Click Me", command=lambda: messagebox.showinfo("value", combobox.get()))
    button.grid(row=1, column=0, padx=5, pady=5)

def images_component(tab):
    image = tk.PhotoImage(file="tree.png")
    button = ttk.Button(tab, image=image, command=lambda: messagebox.showinfo("Image", image.cget("file")))
    button.grid(row=1, column=0, padx=5, pady=5)

def progressbar_component(tab):
    progressbar = ttk.Progressbar(tab, orient=tk.HORIZONTAL, length=200, mode='determinate')
    progressbar.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
    progressbar.start()
    button = ttk.Button(tab, text="progress x 10", command=lambda: progressbar.step(10))
    button.grid(row=1, column=0, padx=5, pady=5)
    button_stop = ttk.Button(tab, text="Cancel", command=lambda: progressbar.stop())
    button_stop.grid(row=1, column=1, padx=5, pady=5)

def create_tabs():
    tabControl = ttk.Notebook(window)
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
    entry_component(tab_entry)
    scrolltext_component(tab_scrolltext)
    combobox_component(tab_combobox)
    images_component(tab_images)
    progressbar_component(tab_progressbar)
    return tabControl

create_tabs()

window.mainloop()