# One-Way Selection Statements

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

if first < 0:
    first = -first

if second < 0:
    second = -second

print("Maximum:", max(first, second))
print("Minimum:", min(first, second))

