import tkinter as tk

def check_fields(event=None):
    
    if username_entry.get().strip() and password_entry.get().strip():
        login_button.config(state="normal")
    else:
        login_button.config(state="disabled")


root = tk.Tk()
root.title("Login Form")


tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)
username_entry.bind("<KeyRelease>", check_fields)


tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)
password_entry.bind("<KeyRelease>", check_fields)


login_button = tk.Button(root, text="Login", state="disabled")
login_button.grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
