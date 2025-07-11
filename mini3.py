import tkinter as tk

def on_key_press(event):
    key_label.config(text=f"Key Pressed: {event.keysym}")
    log_text.insert(tk.END, f"{event.keysym}\n")
    log_text.see(tk.END)  
    if event.keysym == "Escape":
        root.destroy()

root = tk.Tk()
root.title("Live Key Tracker")
root.geometry("300x250")


key_label = tk.Label(root, text="Press any key...", font=("Arial", 14), fg="blue")
key_label.pack(pady=10)

log_text = tk.Text(root, height=10, width=30, state="normal")
log_text.pack(pady=10)


root.bind("<KeyPress>", on_key_press)

root.mainloop()
