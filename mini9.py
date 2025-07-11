import tkinter as tk

def on_enter_label(event):
    event.widget.config(fg="blue", bg="lightgray")

def on_leave_label(event):
    event.widget.config(fg="black", bg="white")

def on_enter_button(event):
    event.widget.config(bg="green", fg="white")

def on_leave_button(event):
    event.widget.config(bg="SystemButtonFace", fg="black")  


root = tk.Tk()
root.title("Mouse Hover Effects")
root.geometry("300x200")


hover_label = tk.Label(root, text="Hover over me!", font=("Arial", 12), bg="white", fg="black", relief="solid", padx=10, pady=5)
hover_label.pack(pady=20)
hover_label.bind("<Enter>", on_enter_label)
hover_label.bind("<Leave>", on_leave_label)

hover_button = tk.Button(root, text="Hover button", font=("Arial", 12))
hover_button.pack(pady=20)
hover_button.bind("<Enter>", on_enter_button)
hover_button.bind("<Leave>", on_leave_button)

root.mainloop()
