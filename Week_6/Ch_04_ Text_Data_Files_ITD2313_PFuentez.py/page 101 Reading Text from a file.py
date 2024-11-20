# Create and write to the file
with open("myfile.txt", 'w') as f:
    f.write("First line.\nSecond line.\n")

# Open the file for reading
f = open("myfile.txt", 'r')

# Read the entire file content
text = f.read()

# Print the content
print(text)

# Close the file
f.close()

# Open the file again for reading
with open("myfile.txt", 'r') as f:
    # Read and print each line
    for line in f:
        print(line, end='')  # end='' to avoid adding extra newlines

# Open the file again for reading
with open("myfile.txt", 'r') as f:
    # Read and print each line until the end of the file
    while True:
        line = f.readline()
        if line == "":
            break
        print(line, end='')  # end='' to avoid adding extra newlines
