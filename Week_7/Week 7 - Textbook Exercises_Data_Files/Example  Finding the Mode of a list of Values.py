file_name = input("Enter the file name: ")
f = open(file_name, 'r')
words = []

for line in f:
    for word in line.split():
        words.append(word.upper())

word_frequencies = {}

for word in words:
    number = word_frequencies.get(word, None)
    if number is None:
        word_frequencies[word] = 1
    else:
        word_frequencies[word] = number + 1

maximum = max(word_frequencies.values())

for key in word_frequencies:
    if word_frequencies[key] == maximum:
        print("The mode is", key)
        break

f.close()
