import tkinter as tk
from tkinter import ttk

class LayoutDemo(tk.Tk):
    """Displays labels in the quadrants.

    The layout of the labels in the window grid are arranged in 2 rows and 2 columns, starting from 0.
    Row 0, column 0: (0, 0)
    Row 0, column 1: (0, 1)
    Row 1, column 0: (1, 0)
    Row 1, column 1: (1, 1)
    """

    def __init__(self):
        """Sets up the window and the labels."""
        super().__init__()
        self.title("Layout Demo")

        self.add_label("(0, 0)", 0, 0)
        self.add_label("(0, 1)", 0, 1)
        self.add_label("(1, 0)", 1, 0)
        self.add_label("(1, 1)", 1, 1)
        self.add_label("(1, 0 and 1)", 1, 0, columnspan=2)

    def add_label(self, text, row, column, columnspan=1):
        label = ttk.Label(self, text=text, borderwidth=1, relief="solid")
        label.grid(row=row, column=column, sticky="nsew", columnspan=columnspan)

if __name__ == "__main__":
    app = LayoutDemo()
    app.mainloop()
