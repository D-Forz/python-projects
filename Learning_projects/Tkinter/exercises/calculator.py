import tkinter as tk
from tkinter import messagebox

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("380x380")
        self.resizable(False, False)
        self.expresion = ""
        self.entry = None
        self.entry_text = tk.StringVar()
        self.create_components()
    
    def create_components(self):
        entry_frame = tk.Frame(self, width=380, height=50, bg='grey')
        entry_frame.pack(side=tk.TOP)
        # Text Entry
        entry = tk.Entry(entry_frame, font=('arial', 18, 'bold'),
                            textvariable=self.entry_text, width=24, justify=tk.RIGHT)
        entry.grid(row=0, column=0, ipady=10)
        # Bottom Frame
        button_frame = tk.Frame(self, width=380, height=380, bg='grey')
        button_frame.pack()
        # First Row
        button_clear = tk.Button(button_frame, text='C', width='32', height=3,
                                    bd=0, bg='#eee', cursor='hand2',
                                    command=self._clear_event)
        button_clear.grid(row=0, column=0, columnspan=3, padx=1,pady=1)
        button_divide = tk.Button(button_frame, text='/', width=10, height=3, bd=0,
                                    bg='#eee', cursor='hand2',
                                    command=lambda: self._click_event('/'))
        button_divide.grid(row=0, column=3, padx=1, pady=1)
        # Second Row
        button_7 = tk.Button(button_frame, text='7', width=10, height=3, bd=0,
                                    bg='#eee', cursor='hand2',
                                    command=lambda: self._click_event('7'))
        button_7.grid(row=1, column=0, padx=1, pady=1)
        button_8 = tk.Button(button_frame, text='8', width=10, height=3, bd=0,
                                    bg='#eee', cursor='hand2',
                                    command=lambda: self._click_event('8'))
        button_8.grid(row=1, column=1, padx=1, pady=1)
        button_9 = tk.Button(button_frame, text='9', width=10, height=3, bd=0,
                                    bg='#eee', cursor='hand2',
                                    command=lambda: self._click_event('9'))
        button_9.grid(row=1, column=2, padx=1, pady=1)
        button_multiply = tk.Button(button_frame, text='*', width=10, height=3, bd=0,
                                    bg='#eee', cursor='hand2',      
                                    command=lambda: self._click_event('*'))
        button_multiply.grid(row=1, column=3, padx=1, pady=1)
        # Third Row
        button_4 = tk.Button(button_frame, text='4', width=10, height=3, bd=0,
                                    bg='#eee', cursor='hand2',      
                                    command=lambda: self._click_event('4'))
        button_4.grid(row=2, column=0, padx=1, pady=1)
        button_5 = tk.Button(button_frame, text='5', width=10, height=3, bd=0,
                                    bg='#eee', cursor='hand2',
                                    command=lambda: self._click_event('5'))
        button_5.grid(row=2, column=1, padx=1, pady=1)
        button_6 = tk.Button(button_frame, text='6', width=10, height=3, bd=0,
                                    bg='#eee', cursor='hand2',              
                                    command=lambda: self._click_event('6'))
        button_6.grid(row=2, column=2, padx=1, pady=1)
        button_minus = tk.Button(button_frame, text='-', width=10, height=3, bd=0,
                                    bg='#eee', cursor='hand2',
                                    command=lambda: self._click_event('-'))
        button_minus.grid(row=2, column=3, padx=1, pady=1)
        # Fourth Row
        button_1 = tk.Button(button_frame, text='1', width=10, height=3, bd=0,
                                    bg='#eee', cursor='hand2',
                                    command=lambda: self._click_event('1'))
        button_1.grid(row=3, column=0, padx=1, pady=1)
        button_2 = tk.Button(button_frame, text='2', width=10, height=3, bd=0,
                                    bg='#eee', cursor='hand2',
                                    command=lambda: self._click_event('2'))
        button_2.grid(row=3, column=1, padx=1, pady=1)
        button_3 = tk.Button(button_frame, text='3', width=10, height=3, bd=0,
                                    bg='#eee', cursor='hand2',  
                                    command=lambda: self._click_event('3'))
        button_3.grid(row=3, column=2, padx=1, pady=1)
        button_plus = tk.Button(button_frame, text='+', width=10, height=3, bd=0,
                                    bg='#eee', cursor='hand2',
                                    command=lambda: self._click_event('+'))
        button_plus.grid(row=3, column=3, padx=1, pady=1)
        # Fifth Row
        button_0 = tk.Button(button_frame, text='0', width=21, height=3, bd=0,
                                    bg='#eee', cursor='hand2',
                                    command=lambda: self._click_event('0'))
        button_0.grid(row=4, column=0, padx=1, pady=1, columnspan=2)
        button_dot = tk.Button(button_frame, text='.', width=10, height=3, bd=0,
                                    bg='#eee', cursor='hand2',
                                    command=lambda: self._click_event('.'))
        button_dot.grid(row=4, column=2, padx=1, pady=1)
        button_equal = tk.Button(button_frame, text='=', width=10, height=3, bd=0,
                                    bg='#eee', cursor='hand2',
                                    command=self._equal_event)
        button_equal.grid(row=4, column=3, padx=1, pady=1)                    
        
        ################################################################################
    def _clear_event(self):
        self.expresion = ''
        self.entry_text.set(self.expresion)
    
    def _click_event(self, value):
        self.expresion = f'{self.expresion}{value}'
        self.entry_text.set(self.expresion)
        
    def _equal_event(self):
        try:
            self.expresion = eval(self.expresion)
            self.entry_text.set(self.expresion)
        except Exception as e:
            messagebox.showerror('Error', e)
            self.entry_text.set('')
        finally:
            self.expresion = ''



if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
