import random

# Open the file in write mode
with open("integers.txt", 'w') as f:
    # Generate and write 500 random integers to the file
    for count in range(500):
        number = random.randint(1, 500)
        f.write(str(number) + '\n')


