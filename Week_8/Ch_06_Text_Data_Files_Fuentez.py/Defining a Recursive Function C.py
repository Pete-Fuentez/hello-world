def summation(lower, upper):
    if lower > upper:
        return 0
    else:
        return lower + summation(lower + 1, upper)

print(summation(5, 20))
print(summation(250, 500))
