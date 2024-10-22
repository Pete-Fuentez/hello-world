# concordance.py

from collections import Counter
import re

def get_words(text):
    """Extract words from a text string and return a list of words in lowercase."""
    return re.findall(r'\b\w+\b', text.lower())

def generate_concordance(filename, n):
    """Generate a concordance of unique words or n-grams from a file."""
    try:
        with open(filename, 'r') as file:
            text = file.read()
            
        # Get the words from the text
        words = get_words(text)

        # Generate n-grams
        n_grams = [' '.join(words[i:i+n]) for i in range(len(words) - n + 1)]
        
        # Count frequencies of n-grams
        n_gram_counts = Counter(n_grams)

        # Sort the n-grams alphabetically and display frequencies
        for n_gram in sorted(n_gram_counts.keys()):
            print(f"{n_gram}: {n_gram_counts[n_gram]}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError:
        print("Invalid input. Please enter a valid number of words.")

def main():
    # Prompt for the filename
    filename = input("Enter the filename: ")
    
    # Prompt for the number of words in the sequence (n)
    try:
        n = int(input("Enter the number of words in the sequence (n): "))
        if n < 1:
            print("Please enter a positive integer for n.")
            return
        generate_concordance(filename, n)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
