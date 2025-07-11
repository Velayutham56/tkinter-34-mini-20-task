import tkinter as tk

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        self.tasks = []
        self.listbox = tk.Listbox(root, font=("Arial", 16), width=40, height=10)
        self.listbox.pack(pady=20)

        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=5)

        add_btn = tk.Button(root, text="Add Task", command=self.add_task)
        add_btn.pack(pady=5)

        self.listbox.bind("<Double-Button-1>", self.toggle_task)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)

    def toggle_task(self, event):
        index = self.listbox.curselection()
        if index:
            idx = index[0]
            task_text = self.listbox.get(idx)

            if task_text.startswith("✔ "):
                new_text = task_text[2:]  
                self.listbox.delete(idx)
                self.listbox.insert(idx, new_text)
                self.listbox.itemconfig(idx, {'fg': 'black'})
            else:
                new_text = f"✔ {task_text}"
                self.listbox.delete(idx)
                self.listbox.insert(idx, new_text)
                self.listbox.itemconfig(idx, {'fg': 'green'})

root = tk.Tk()
app = TaskManager(root)
root.mainloop()
