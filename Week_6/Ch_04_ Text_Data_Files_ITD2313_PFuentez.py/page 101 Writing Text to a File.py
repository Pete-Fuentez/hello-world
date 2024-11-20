# Open a file named 'myfile.txt' in write mode
with open('myfile.txt', 'w') as file:
    # Write two lines of text to the file
    file.write('This is the first line.\n')
    file.write('This is the second line.\n')

# Open the same file in read mode to verify the content
with open('myfile.txt', 'r') as file:
    # Read the contents of the file
    content = file.read()
    # Print the contents to the console
    print(content)
