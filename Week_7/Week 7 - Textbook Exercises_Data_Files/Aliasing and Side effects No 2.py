# code 1 of 3
first = [10, 20, 30]
second = first
print(first)
print(second)
first[1] = 99
print(first)
print(second)

print("-----------------")

# code 2 of 3
third = []
for element in first:
    third.append(element)
print(first)
print(third)
first[1] = 100
print(first)
print(third)
