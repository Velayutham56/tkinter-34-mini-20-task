import tkinter as tk

def draw_circle(event):
    x, y = event.x, event.y
    radius = 20
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="skyblue")
    coords_label.config(text=f"Circle at: ({x}, {y})")

def draw_rectangle(event):
    x, y = event.x, event.y
    width, height = 40, 30
    canvas.create_rectangle(x, y, x + width, y + height, fill="lightgreen")
    coords_label.config(text=f"Rectangle at: ({x}, {y})")

root = tk.Tk()
root.title("Shape Drawer Canvas")
root.geometry("400x400")


canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

coords_label = tk.Label(root, text="Click to draw a shape", font=("Arial", 12))
coords_label.pack(pady=10)


canvas.bind("<Button-1>", draw_circle)    
canvas.bind("<Button-3>", draw_rectangle) 

root.mainloop()
