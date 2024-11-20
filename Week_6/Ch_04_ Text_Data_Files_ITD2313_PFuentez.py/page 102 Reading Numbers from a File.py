with open("integers.txt", 'r') as f:
    the_sum = 0
    for line in f:
        line = line.strip()
        number = int(line)
        the_sum += number
    print("The sum is", the_sum)

with open("integers.txt", 'r') as f:
    the_sum = 0
    for line in f:
        word_list = line.split()
        for word in word_list:
            number = int(word)
            the_sum += number
    print("The sum is", the_sum)
