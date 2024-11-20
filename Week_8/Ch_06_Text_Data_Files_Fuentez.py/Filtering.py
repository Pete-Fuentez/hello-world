def odd(n):
    return n % 2 == 1

result = list(filter(odd, range(10)))
print(result)
