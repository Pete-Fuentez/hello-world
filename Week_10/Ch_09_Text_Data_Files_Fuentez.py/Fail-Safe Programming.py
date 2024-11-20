"""
file: guessversion1.py
a prototype that lays out the user interface for a GUI-based
guessing game.
"""

import random
from breezypythongui import EasyFrame

class GuessingGame(EasyFrame):
    """Plays a guessing game with the user."""

    def __init__(self):
        """Sets up the window, widgets, and data."""
        EasyFrame.__init__(self, title="Guessing Game")
        # Initialize the instance variables for the data
        self.myNumber = random.randint(1, 100)
        self.count = 0

        # Create and add widgets to the window
        greeting = "Guess a number between 1 and 100."
        self.hintLabel = self.addLabel(text=greeting,
                                       row=0, column=0,
                                       sticky="NSEW",
                                       columnspan=2)
        self.addLabel(text="Your guess", row=1, column=0)
        self.guessField = self.addIntegerField(0, row=1, column=1)

        # Buttons with command attributes
        self.nextButton = self.addButton(text="Next", row=2, column=0, command=self.nextGuess)
        self.newButton = self.addButton(text="New Game", row=2, column=1, command=self.newGame)

    def nextGuess(self):
        """Processes the user's next guess."""
        guess = self.guessField.getNumber()
        result = self.validate_input(guess)
        
        if isinstance(result, int):
            self.count += 1
            guess = result
            if guess == self.myNumber:
                self.hintLabel["text"] = f"You've guessed it in {self.count} attempts!"
                self.nextButton["state"] = "disabled"
            elif guess < self.myNumber:
                self.hintLabel["text"] = "Sorry, too small!"
            else:
                self.hintLabel["text"] = "Sorry, too large!"
        else:
            self.hintLabel["text"] = f"Error: {result}"

    def newGame(self):
        """Resets the data and GUI to their original states."""
        self.myNumber = random.randint(1, 100)
        self.count = 0
        greeting = "Guess a number between 1 and 100."
        self.hintLabel["text"] = greeting
        self.guessField.setNumber(0)
        self.nextButton["state"] = "normal"

    def validate_input(self, input_value):
        """Validates the input to ensure it is an integer greater than or equal to 0."""
        try:
            num = int(input_value)
            if num >= 0:
                return num
            else:
                raise ValueError("Input must be an integer greater than or equal to 0.")
        except ValueError as e:
            return str(e)

def main():
    """Instantiate and pop up the window."""
    GuessingGame().mainloop()

if __name__ == "__main__":
    main()
