def displayRange(lower, upper):
    if lower <= upper:
        print(lower)
        displayRange(lower + 1, upper)

displayRange(5, 10)
print("---------")
displayRange(15, 20)
