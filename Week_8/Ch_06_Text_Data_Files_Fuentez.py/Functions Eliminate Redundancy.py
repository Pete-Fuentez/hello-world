def summation(lower, upper):
    """
    Arguments:
    - lower: a lower bound
    - upper: an upper bound
    
    Returns:
    - The sum of the numbers from lower through upper
    """
    result = 0
    while lower <= upper:
        result += lower
        lower += 1
    return result

print(summation(1, 4))
print(summation(50, 100))
