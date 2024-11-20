# Line 1
name = "Alan Turing"

# Line 2
print(name[0])  # Examine the first character. Output: 'A'

# Line 3
print(name[3])  # Examine the fourth character. Output: 'n'

# Line 4
# This will raise an IndexError because the length of name is 11 (indices 0-10).
# So accessing name[len(name)] will result in an error.
try:
    print(name[len(name)])  # Oops! This will cause an error.
except IndexError as e:
    print("A string index out of range error is displayed.")  # Handle the error.

# Line 5
print(name[len(name) - 1])  # Examine the last character. Output: 'g'

# Line 6
print(name[-1])  # Shorthand for the last character. Output: 'g'

# Line 7
print(name[-2])  # Shorthand for the next to last character. Output: 'n'
