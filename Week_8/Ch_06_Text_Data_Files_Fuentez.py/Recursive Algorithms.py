def printRange(lower, upper):
    if lower <= upper:
        print(lower)
        printRange(lower + 1, upper)

printRange(2, 10)
print("-----")
printRange(20, 30)

print("---second code---")
 
def summation(lower, upper):
    if lower > upper:
        return 0
    else:
        return lower + summation(lower + 1, upper)

print(summation(1, 4))
print("-----")
print(summation(50, 100))
