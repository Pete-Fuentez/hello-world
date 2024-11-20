# Open the file for input
with open('myfile.txt', 'r') as file:
    # Read all lines
    lines = file.readlines()
    # Print the number of lines
    print(f'The number of lines in the file is: {len(lines)}')

# Open the file for input
with open('myfile.txt', 'r') as file:
    # Read the entire file
    content = file.read()
    # Split the content into words
    words = content.split()
    # Count the number of four-letter words
    four_letter_words = [word for word in words if len(word) == 4]
    print(f'The number of four-letter words in the file is: {len(four_letter_words)}')

# Open the file for input
with open('integers.txt', 'r') as file:
    # Read the integers from the file
    numbers = [int(line) for line in file]
    # Calculate the average
    if numbers:
        average = sum(numbers) / len(numbers)
        print(f'The average value of the integers is: {average}')
    else:
        print('The file is empty.')

import os

# Get the list of items in the current working directory
items = os.listdir()
# Print the names of all items
print('Items in the current directory:')
for item in items:
    print(item)

import os

# Prompt the user for a filename
filename = input('Enter the filename: ')

# Check if the file exists
if os.path.isfile(filename):
    # Open and print the contents of the file
    with open(filename, 'r') as file:
        print(file.read())
else:
    print(f'Error: The file "{filename}" does not exist.')


