import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Calculator")
        self.root.geometry("300x400")

        self.entry = tk.Entry(root, font=("Arial", 24), bd=8, relief=tk.RIDGE, justify="right")
        self.entry.pack(fill=tk.BOTH, padx=10, pady=10)

        self.create_buttons()

        
        self.root.bind("<Key>", self.key_input)

    def create_buttons(self):
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]
        for row_vals in buttons:
            row = tk.Frame(self.root)
            row.pack(expand=True, fill='both')
            for val in row_vals:
                b = tk.Button(row, text=val, font=("Arial", 18), relief=tk.GROOVE, command=lambda v=val: self.click(v))
                b.pack(side='left', expand=True, fill='both')

    def click(self, value):
        if value == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, value)

    def key_input(self, event):
        char = event.char
        if char in '0123456789.+-*/':
            self.entry.insert(tk.END, char)
        elif char == '\r':  
            self.click('=')

root = tk.Tk()
calc = Calculator(root)
root.mainloop()
