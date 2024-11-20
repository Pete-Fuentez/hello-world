"""
file: decrypt.py
Decrypts an input string of lowercase letters and prints 
the result. The other input is the distance value.
"""

# Line 22
code = input("Enter the coded text: ")

# Line 23
distance = int(input("Enter the distance value: "))

# Line 24
plaintext = ""

# Line 25
for ch in code:
    # Line 26
    ord_value = ord(ch)
    
    # Line 27
    cipher_value = ord_value - distance
    
    # Line 28
    if cipher_value < ord('a'):
        # Line 29
        cipher_value = ord('z') - (distance - (ord_value - ord('a') - 1))
    
    # Line 31
    plaintext += chr(cipher_value)

# Line 32
print(plaintext)
