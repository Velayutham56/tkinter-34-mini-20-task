import tkinter as tk

def check_selections():
    if question1_var.get() != 0 and question2_var.get() != 0:
        next_button.config(state="normal")
    else:
        next_button.config(state="disabled")

root = tk.Tk()
root.title("Survey Form")


tk.Label(root, text="1. What is your favorite color?").grid(row=0, column=0, sticky="w", padx=10, pady=5)
question1_var = tk.IntVar()
question1_var.set(0)
colors = ["Red", "Blue", "Green"]
for i, color in enumerate(colors, start=1):
    tk.Radiobutton(root, text=color, variable=question1_var, value=i, command=check_selections).grid(row=i, column=0, sticky="w", padx=20)


tk.Label(root, text="2. Do you like Python?").grid(row=5, column=0, sticky="w", padx=10, pady=5)
question2_var = tk.IntVar()
question2_var.set(0)
answers = ["Yes", "No"]
for i, answer in enumerate(answers, start=1):
    tk.Radiobutton(root, text=answer, variable=question2_var, value=i, command=check_selections).grid(row=5+i, column=0, sticky="w", padx=20)


next_button = tk.Button(root, text="Next", state="disabled")
next_button.grid(row=8, column=0, pady=20)

root.mainloop()
