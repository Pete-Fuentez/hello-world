"""
file: encrypt.py
Encrypts an input string of lowercase letters and prints 
the result. The other input is the distance value.
"""

# Line 6
plaintext = input("Enter a one-word, lowercase message: ")

# Line 7
distance = int(input("Enter the distance value: "))

# Line 8
code = ""

# Line 9
for ch in plaintext:
    # Line 10
    ord_value = ord(ch)
    
    # Line 11
    cipher_value = ord_value + distance
    
    # Line 12
    if cipher_value > ord('z'):
        # Line 13
        cipher_value = ord('a') + distance - (ord('z') - ord_value + 1)
    
    # Line 15
    code += chr(cipher_value)

# Line 16
print(code)
