import tkinter as tk

def add_tooltip(widget, text):
    tooltip = tk.Label(widget.master, text=text, bg="lightyellow", relief="solid", borderwidth=1, padx=5, pady=2)
    
    def show_tip(event):
        
        x = event.widget.winfo_rootx() + 20
        y = event.widget.winfo_rooty() + 20
        tooltip.place(x=x, y=y)

    def hide_tip(event):
        tooltip.place_forget()
    
    widget.bind("<Enter>", show_tip)
    widget.bind("<Leave>", hide_tip)


root = tk.Tk()
root.title("Hover Tooltip Example")
root.geometry("300x200")

btn1 = tk.Button(root, text="Submit")
btn1.pack(pady=20)
add_tooltip(btn1, "Click to submit your data.")

entry1 = tk.Entry(root)
entry1.pack(pady=20)
add_tooltip(entry1, "Enter your name here.")

root.mainloop()
