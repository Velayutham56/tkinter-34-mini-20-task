import tkinter as tk


direction_colors = {
    "Left": "red",
    "Right": "green",
    "Up": "blue",
    "Down": "yellow"
}

def change_color(event):
    direction = event.keysym
    if direction in direction_colors:
        new_color = direction_colors[direction]
        color_frame.config(bg=new_color)
        color_label.config(text=f"Current Color: {new_color.capitalize()}")


root = tk.Tk()
root.title("Dynamic Color Picker")
root.geometry("300x200")


color_frame = tk.Frame(root, width=300, height=150, bg="white")
color_frame.pack(fill="both", expand=True)


color_label = tk.Label(root, text="Current Color: White", font=("Arial", 12))
color_label.pack(pady=10)


root.bind("<Left>", change_color)
root.bind("<Right>", change_color)
root.bind("<Up>", change_color)
root.bind("<Down>", change_color)

root.mainloop()
