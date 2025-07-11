import tkinter as tk

class CharCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Character Counter")

        self.entry = tk.Entry(root, font=("Arial", 16), width=30)
        self.entry.pack(pady=20)
        self.entry.bind("<KeyRelease>", self.update_count)

        self.count_label = tk.Label(root, text="Characters: 0", font=("Arial", 14))
        self.count_label.pack(pady=10)

    def update_count(self, event=None):
        text = self.entry.get()
        count = len(text)
        self.count_label.config(text=f"Characters: {count}")

root = tk.Tk()
app = CharCounterApp(root)
root.mainloop()
