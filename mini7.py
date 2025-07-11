import tkinter as tk
import re


EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"

def validate_email(event=None):
    email = email_entry.get().strip()
    if re.match(EMAIL_REGEX, email):
        submit_btn.config(state="normal")
        status_label.config(text="✅ Valid Email", fg="green")
    else:
        submit_btn.config(state="disabled")
        status_label.config(text="❌ Invalid Email", fg="red")


root = tk.Tk()
root.title("Email Validator")
root.geometry("300x150")


tk.Label(root, text="Enter your email:").pack(pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.pack()
email_entry.bind("<KeyRelease>", validate_email)


status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.pack(pady=5)

submit_btn = tk.Button(root, text="Submit", state="disabled")
submit_btn.pack(pady=10)

root.mainloop()
