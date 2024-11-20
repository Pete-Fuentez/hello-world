"""
file: decimal_to_binary.py
converts a decimal integer to a string of bits.
"""

decimal = int(input("Enter a decimal integer: "))
if decimal == 0:
    print(0)
else:
    print("quotient remainder binary")
    bitstring = ""
    
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        bitstring = str(remainder) + bitstring
        print("%5d %8d %12s" % (decimal, remainder, bitstring))

    print("The binary representation is", bitstring)
