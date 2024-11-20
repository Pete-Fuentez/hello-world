# accepts only valid inputs for our grade conversion script and displays an error message otherwise
number = int(input("Enter the numeric grade: "))

if number > 89:
    letter = 'A'
elif number > 79:
    letter = 'B'
elif number > 69:
    letter = 'C'
else:
    letter = 'F'

print("The letter grade is", letter)
