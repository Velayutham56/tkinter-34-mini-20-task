import tkinter as tk

def show_dialog():
    
    name = entry_name.get()
    email = entry_email.get()

   
    dialog = tk.Toplevel(root)
    dialog.title("Form Submitted")
    dialog.geometry("250x150")
    dialog.transient(root)  

    
    lbl_info = tk.Label(dialog, text=f"Name: {name}\nEmail: {email}", padx=10, pady=10)
    lbl_info.pack()

    
    btn_close = tk.Button(dialog, text="Close", command=dialog.destroy)
    btn_close.pack(pady=10)

root = tk.Tk()
root.title("Form Example")
root.geometry("300x200")


tk.Label(root, text="Name:").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Email:").pack(pady=5)
entry_email = tk.Entry(root)
entry_email.pack()


submit_btn = tk.Button(root, text="Submit", command=show_dialog)
submit_btn.pack(pady=20)

root.mainloop()
