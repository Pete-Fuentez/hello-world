# stats.py

from collections import Counter

def mean(numbers):
    """Compute the average of a list of numbers."""
    if not numbers:  # Check if the list is empty
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    """Compute the median of a list of numbers."""
    if not numbers:  # Check if the list is empty
        return 0
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:  # If even number of elements
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:  # If odd number of elements
        return sorted_numbers[mid]

def mode(numbers):
    """Compute the mode of a list of numbers."""
    if not numbers:  # Check if the list is empty
        return 0
    count = Counter(numbers)
    max_count = max(count.values())
    modes = [num for num, cnt in count.items() if cnt == max_count]
    return modes[0]  # Return the first mode found (arbitrary choice if multiple modes)

def main():
    # Test the functions with a sample list
    sample_numbers = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    
    print("Sample numbers:", sample_numbers)
    print("Mean:", mean(sample_numbers))
    print("Median:", median(sample_numbers))
    print("Mode:", mode(sample_numbers))

if __name__ == "__main__":
    main()
