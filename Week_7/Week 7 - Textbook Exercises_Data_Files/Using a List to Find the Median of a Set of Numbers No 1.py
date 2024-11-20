"""
file: median.py
Prints the median of a set of numbers in a file.
"""

file_name = input("Enter the file name: ")

try:
    with open(file_name, 'r') as f:
        numbers = []
        for line in f:
            words = line.split()
            for word in words:
                try:
                    numbers.append(float(word))
                except ValueError:
                    print(f"Warning: '{word}' is not a number and will be ignored.")
        
        if not numbers:
            print("No valid numbers found in the file.")
        else:
            numbers.sort()
            midpoint = len(numbers) // 2
            print("The median is", end=" ")
            if len(numbers) % 2 == 1:
                print(numbers[midpoint])
            else:
                print((numbers[midpoint] + numbers[midpoint - 1]) / 2)
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
