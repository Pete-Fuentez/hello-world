def average(lyst):
    """Returns the average of the numbers in lyst."""
    the_sum = 0
    for number in lyst:
        the_sum += number
    return the_sum / len(lyst)

print(average([1, 2, 3, 4, 5]))
