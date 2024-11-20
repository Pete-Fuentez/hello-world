"""
File: testinputfunctions.py

Defines functions for robust input of ints and floats.
"""

def inputInt(prompt):
    """Guarantees that the user inputs an integer,
    using the given prompt. Returns the integer."""
    while True:
        theString = input(prompt)
        if theString.isdigit():
            return int(theString)
        else:
            print("Error: the input must consist only of digits")

def inputFloat(prompt):
    """Guarantees that the user inputs a floating-point number,
    using the given prompt. Returns the float."""
    while True:
        user_input = input(prompt)
        if user_input.replace('.', '', 1).isdigit() and user_input.count('.') <= 1:
            return float(user_input)
        else:
            print("Error: the input must be a valid floating-point number.")

def main():
    n = inputInt("Please enter an integer: ")
    print(f"You entered the integer: {n}")
    
    f = inputFloat("Please enter a floating-point number: ")
    print(f"You entered the float: {f}")

if __name__ == "__main__":
    main()
