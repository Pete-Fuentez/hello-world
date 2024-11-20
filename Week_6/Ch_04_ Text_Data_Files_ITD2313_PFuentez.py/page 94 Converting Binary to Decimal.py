"""
file: binary_to_decimal.py
converts a string of bits to a decimal integer.
"""

bitstring = input("Enter a string of bits: ")
decimal = 0
exponent = len(bitstring) - 1

for digit in bitstring:
    decimal += int(digit) * 2 ** exponent
    exponent -= 1

print("The integer value is", decimal)
