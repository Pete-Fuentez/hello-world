from functools import reduce

def summation(lower, upper):
    return reduce(lambda x, y: x + y, range(lower, upper + 1))

print(summation(5, 10))
