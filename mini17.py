import tkinter as tk

STEP = 10

def move_object(event):
    key = event.keysym
    x1, y1, x2, y2 = canvas.coords(shape)  

    if key == "Up" and y1 > 0:
        canvas.move(shape, 0, -STEP)
    elif key == "Down" and y2 < canvas.winfo_height():
        canvas.move(shape, 0, STEP)
    elif key == "Left" and x1 > 0:
        canvas.move(shape, -STEP, 0)
    elif key == "Right" and x2 < canvas.winfo_width():
        canvas.move(shape, STEP, 0)


root = tk.Tk()
root.title("Canvas Object Mover")
root.geometry("400x400")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

shape = canvas.create_oval(150, 150, 200, 200, fill="blue") 


root.bind("<KeyPress>", move_object)

root.mainloop()
