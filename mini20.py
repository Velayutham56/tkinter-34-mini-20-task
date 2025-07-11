import tkinter as tk

class EmojiBar(tk.Frame):
    def __init__(self, master, callback=None, **kwargs):
        super().__init__(master, **kwargs)
        self.callback = callback  
        self.emojis = ["😀", "😢", "😠", "❤️", "👍", "👎"]
        
        for emoji in self.emojis:
            btn = tk.Button(self, text=emoji, font=("Arial", 14), width=3,
                            command=lambda e=emoji: self.react(e))
            btn.pack(side="left", padx=2)

    def react(self, emoji):
        if self.callback:
            self.callback(emoji)
        else:
            print(f"Reacted with: {emoji}")


def update_reaction(emoji):
    reaction_lbl.config(text=f"Selected Reaction: {emoji}")


root = tk.Tk()
root.title("Emoji Reaction Panel")
root.geometry("400x200")

tk.Label(root, text="Message 1").pack(pady=5)
reaction_lbl = tk.Label(root, text="Selected Reaction: None", fg="blue")
reaction_lbl.pack()


emoji_bar1 = EmojiBar(root, callback=update_reaction)
emoji_bar1.pack(pady=10)

tk.Label(root, text="Message 2").pack(pady=5)


emoji_bar2 = EmojiBar(root)
emoji_bar2.pack(pady=10)

root.mainloop()
