from functools import reduce

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

data = [1, 2, 3, 4]

result_add = reduce(add, data)
print(result_add)

result_multiply = reduce(multiply, data)
print(result_multiply)
