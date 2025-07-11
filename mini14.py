import tkinter as tk

class Notification(tk.Frame):
    def __init__(self, master, message, bg_color="lightblue", duration=5000, icon="🔔"):
        super().__init__(master, bg=bg_color, padx=10, pady=5)
        self.pack_propagate(False)

        self.icon_label = tk.Label(self, text=icon, bg=bg_color, font=("Arial", 16))
        self.icon_label.pack(side=tk.LEFT)

        self.message_label = tk.Label(self, text=message, bg=bg_color, font=("Arial", 14))
        self.message_label.pack(side=tk.LEFT, padx=(5, 10))

        self.close_button = tk.Button(self, text="✖", command=self.destroy, bg=bg_color, relief=tk.FLAT)
        self.close_button.pack(side=tk.RIGHT)

        self.place(x=0, y=0, relwidth=1)
        self.after(duration, self.destroy)


root = tk.Tk()
root.geometry("400x300")

tk.Button(root, text="Show Notification", command=lambda: Notification(root, "New message received!")).pack(pady=50)

root.mainloop()
