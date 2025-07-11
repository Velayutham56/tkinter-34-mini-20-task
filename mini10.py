import tkinter as tk

def on_key_press(event):
    current = listbox.curselection()
    if event.keysym == "Down":
        if current:
            next_index = min(current[0] + 1, listbox.size() - 1)
        else:
            next_index = 0
        listbox.selection_clear(0, tk.END)
        listbox.selection_set(next_index)
        listbox.activate(next_index)
    elif event.keysym == "Up":
        if current:
            prev_index = max(current[0] - 1, 0)
        else:
            prev_index = 0
        listbox.selection_clear(0, tk.END)
        listbox.selection_set(prev_index)
        listbox.activate(prev_index)
    elif event.keysym == "Return":
        if current:
            selected = listbox.get(current[0])
            display_label.config(text=f"Selected: {selected}")


root = tk.Tk()
root.title("Listbox Navigator")
root.geometry("300x250")


listbox = tk.Listbox(root, height=8)
items = ["Python", "Java", "C++", "JavaScript", "Ruby", "Go", "Swift", "Rust"]
for item in items:
    listbox.insert(tk.END, item)
listbox.pack(pady=10)


display_label = tk.Label(root, text="Selected: None", font=("Arial", 12))
display_label.pack()


root.bind("<Up>", on_key_press)
root.bind("<Down>", on_key_press)
root.bind("<Return>", on_key_press)

root.mainloop()
