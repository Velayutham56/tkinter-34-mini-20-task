import tkinter as tk

def toggle_state():
    new_state = 'disabled' if toggle_btn['text'] == 'Disable Panel' else 'normal'
    toggle_btn.config(text='Enable Panel' if new_state == 'disabled' else 'Disable Panel')

    for widget in panel_frame.winfo_children():
        try:
            widget.config(state=new_state)
        except tk.TclError:
            pass  

root = tk.Tk()
root.title("Resizable Panel with State Control")
root.geometry("400x300")


panel_frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)
panel_frame.pack(expand=True, fill='both', padx=10, pady=10)


entries = [tk.Entry(panel_frame) for _ in range(3)]
buttons = [tk.Button(panel_frame, text=f"Action {i+1}") for i in range(2)]

for widget in entries + buttons:
    widget.pack(pady=5, padx=10)


toggle_btn = tk.Button(root, text="Disable Panel", command=toggle_state)
toggle_btn.pack(pady=10)

root.mainloop()
