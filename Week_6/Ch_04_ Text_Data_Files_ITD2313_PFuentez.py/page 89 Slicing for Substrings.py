# Line 1
name = "my file.txt"  # The entire string

# Line 2
print(name[0:])  # Output: 'my file.txt'

# Line 3
print(name[0:1])  # The first character. Output: 'm'

# Line 4
print(name[0:2])  # The first two characters. Output: 'my'

# Line 5
print(name[:len(name)])  # The entire string. Output: 'my file.txt'

# Line 6
print(name[2:6])  # Extract 'file'. Output: 'file'

# Line 7
print(name[-3:])  # The last three characters. Output: 'txt'
