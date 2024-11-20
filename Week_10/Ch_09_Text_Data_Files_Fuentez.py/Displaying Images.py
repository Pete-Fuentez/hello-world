from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font

class ImageDemo(EasyFrame):
    """Displays an image and a caption."""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title="Image Demo")
        self.setResizable(False)
        
        image_label = self.addLabel(text="", row=0, column=0, sticky="nsew")
        text_label = self.addLabel(text="Smokey the Cat", row=1, column=0, sticky="nsew")

        # Load the image and associate it with the image label
        self.image = PhotoImage(file="C:/Users/fuent/Documents/Script program/weekly/Week_10/Ch_09_Text_Data_Files_Fuentez.py/PhotoImage/smokey.gif")
        image_label["image"] = self.image

        # Set the font and color of the caption
        font = Font(family="Verdana", size=15, slant="italic")
        text_label["font"] = font
        text_label["foreground"] = "blue"

if __name__ == "__main__":
    app = ImageDemo()
    app.setSize(250, 200)
    app.mainloop()
