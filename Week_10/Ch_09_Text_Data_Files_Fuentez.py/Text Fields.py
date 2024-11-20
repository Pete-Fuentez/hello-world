import tkinter as tk

class TextFieldDemo(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Text Field Demo")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.add_label(text="Input", row=0, column=0)
        self.inputfield = self.add_text_field(text="", row=0, column=1)
        self.add_label(text="Output", row=1, column=0)
        self.outputfield = self.add_text_field(text="", row=1, column=1, state="readonly")
        self.add_button(text="Convert", row=2, column=0, columnspan=2, command=self.convert)

    def add_label(self, **kwargs):
        label = tk.Label(self, text=kwargs['text'])
        label.grid(row=kwargs['row'], column=kwargs['column'], padx=10, pady=10)
        return label

    def add_text_field(self, **kwargs):
        entry = tk.Entry(self, text=kwargs['text'], width=70)
        entry.grid(row=kwargs['row'], column=kwargs['column'], padx=10, pady=10)
        if 'state' in kwargs:
            entry.config(state=kwargs['state'])
        return entry

    def add_button(self, **kwargs):
        button = tk.Button(self, text=kwargs['text'], command=kwargs['command'])
        button.grid(row=kwargs['row'], column=kwargs['column'], columnspan=kwargs['columnspan'], pady=10)
        return button

    def convert(self):
        text = self.inputfield.get()
        result = text.upper()
        self.outputfield.config(state="normal")
        self.outputfield.delete(0, tk.END)
        self.outputfield.insert(0, result)
        self.outputfield.config(state="readonly")

root = tk.Tk()
app = TextFieldDemo(master=root)
app.mainloop()
