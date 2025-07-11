import tkinter as tk

class ToggleSwitch(tk.Frame):
    def __init__(self, master=None, initial_state=False, **kwargs):
        super().__init__(master, **kwargs)
        self.state = initial_state

        
        self.label = tk.Label(self, text="OFF" if not self.state else "ON", font=("Arial", 12), width=6)
        self.label.pack(side="left", padx=5)

      
        self.button = tk.Button(self, text="Toggle", command=self.toggle_state)
        self.button.pack(side="right", padx=5)

    def toggle_state(self):
        self.state = not self.state
        self.label.config(text="ON" if self.state else "OFF")


root = tk.Tk()
root.title("Custom Toggle Widget")

toggle1 = ToggleSwitch(root, bg="lightgray")
toggle1.pack(pady=10)

toggle2 = ToggleSwitch(root, bg="lightblue")
toggle2.pack(pady=10)

toggle3 = ToggleSwitch(root, bg="lightgreen")
toggle3.pack(pady=10)

root.mainloop()
