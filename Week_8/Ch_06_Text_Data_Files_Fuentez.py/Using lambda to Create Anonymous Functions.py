from functools import reduce

data = [1, 2, 3, 4]

result_add = reduce(lambda x, y: x + y, data)
print(result_add)

result_multiply = reduce(lambda x, y: x * y, data)
print(result_multiply)
