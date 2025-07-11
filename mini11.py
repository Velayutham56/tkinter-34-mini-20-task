import tkinter as tk

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Timer")

        self.time = 0
        self.running = False

        self.label = tk.Label(root, text="0", font=("Arial", 40))
        self.label.pack(pady=20)

        button_frame = tk.Frame(root)
        button_frame.pack()

        self.start_btn = tk.Button(button_frame, text="Start", command=self.start)
        self.start_btn.grid(row=0, column=0, padx=5)

        self.stop_btn = tk.Button(button_frame, text="Stop", command=self.stop, state=tk.DISABLED)
        self.stop_btn.grid(row=0, column=1, padx=5)

        self.reset_btn = tk.Button(button_frame, text="Reset", command=self.reset)
        self.reset_btn.grid(row=0, column=2, padx=5)

    def update_timer(self):
        if self.running:
            self.time += 1
            self.label.config(text=str(self.time))
            self.root.after(1000, self.update_timer)

    def start(self):
        if not self.running:
            self.running = True
            self.start_btn.config(state=tk.DISABLED)
            self.stop_btn.config(state=tk.NORMAL)
            self.update_timer()

    def stop(self):
        if self.running:
            self.running = False
            self.start_btn.config(state=tk.NORMAL)
            self.stop_btn.config(state=tk.DISABLED)

    def reset(self):
        self.running = False
        self.time = 0
        self.label.config(text="0")
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)

root = tk.Tk()
app = TimerApp(root)
root.mainloop()
