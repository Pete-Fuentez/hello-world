income = float(input("Enter your income: "))
tax_rate = float(input("Enter the tax rate (as a decimal): "))

tax = income * tax_rate
tax = round(tax, 2)

print("The tax is:", tax)
