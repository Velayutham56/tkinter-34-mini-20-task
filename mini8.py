import tkinter as tk

class CounterWidget(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.count = 0

       
        self.label = tk.Label(self, text=f"Count: {self.count}", font=("Arial", 14))
        self.label.pack(pady=5)

  
        btn_frame = tk.Frame(self)
        btn_frame.pack()

        self.inc_btn = tk.Button(btn_frame, text="Increment", command=self.increment)
        self.inc_btn.pack(side="left", padx=5)

        self.dec_btn = tk.Button(btn_frame, text="Decrement", command=self.decrement)
        self.dec_btn.pack(side="left", padx=5)

        self.reset_btn = tk.Button(btn_frame, text="Reset", command=self.reset)
        self.reset_btn.pack(side="left", padx=5)

    def update_label(self):
        self.label.config(text=f"Count: {self.count}")

    def increment(self):
        self.count += 1
        self.update_label()

    def decrement(self):
        self.count -= 1
        self.update_label()

    def reset(self):
        self.count = 0
        self.update_label()


root = tk.Tk()
root.title("Custom Counter Widget")


counter1 = CounterWidget(root, bg="lightyellow", bd=2, relief="groove")
counter1.pack(pady=10)

counter2 = CounterWidget(root, bg="lavender", bd=2, relief="ridge")
counter2.pack(pady=10)

root.mainloop()
