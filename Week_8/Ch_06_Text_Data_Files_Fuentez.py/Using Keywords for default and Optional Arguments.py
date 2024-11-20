def rep_to_int(rep_string, base):
    decimal = 0
    exponent = len(rep_string) - 1
    for digit in rep_string:
        if digit.isdigit():
            decimal += int(digit) * base ** exponent
        else:
            decimal += (ord(digit.upper()) - ord('A') + 10) * base ** exponent
        exponent -= 1
    return decimal

print(rep_to_int('101', 2), rep_to_int('A3', 16), rep_to_int('123', 8))

