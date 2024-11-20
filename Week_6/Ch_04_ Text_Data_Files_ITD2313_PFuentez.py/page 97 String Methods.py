sentence = input("Enter a sentence: ")
# Output: Enter a sentence: this sentence has no long words.

list_of_words = sentence.split()

print("There are", len(list_of_words), "words.")
# Output: There are 6 words.

sum = 0
for word in list_of_words:
    sum += len(word)

print("The average word length is", sum / len(list_of_words))
# Output: The average word length is 4.5
