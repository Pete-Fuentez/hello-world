number = int(input("Enter the numeric grade: "))

if number > 100:
    print("Error: grade must be between 100 and 0")
elif number < 0:
    print("Error: grade must be between 100 and 0")
else:
    print("This is a valid grade.")
