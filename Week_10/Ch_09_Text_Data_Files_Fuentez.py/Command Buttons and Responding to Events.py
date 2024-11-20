import tkinter as tk

class ButtonDemo(tk.Frame):
    """Illustrates command buttons and user events."""

    def __init__(self, master=None):
        """Sets up the window, label, and buttons."""
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Hello, world!")
        self.label.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.clear_btn = tk.Button(self, text="Clear", command=self.clear_label)
        self.clear_btn.grid(row=1, column=0)

        self.restore_btn = tk.Button(self, text="Restore", command=self.restore_label, state="disabled")
        self.restore_btn.grid(row=1, column=1)

    def clear_label(self):
        self.label["text"] = ""
        self.clear_btn["state"] = "disabled"
        self.restore_btn["state"] = "normal"

    def restore_label(self):
        self.label["text"] = "Hello, world!"
        self.clear_btn["state"] = "normal"
        self.restore_btn["state"] = "disabled"

root = tk.Tk()
root.title("Button Demo")
app = ButtonDemo(master=root)
app.mainloop()
