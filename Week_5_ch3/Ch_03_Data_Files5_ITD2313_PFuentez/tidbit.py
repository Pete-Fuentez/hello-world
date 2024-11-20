purchase_price = float(input("Enter the purchase price: "))

down_payment = 0.10 * purchase_price
annual_interest_rate = 0.12
monthly_payment = 0.05 * purchase_price

balance = purchase_price - down_payment

print("\nMonth\tBalance Owed\tInterest Owed\tPrincipal Owed\tPayment\t\tRemaining Balance")
print("-------------------------------------------------------------------------------")

month = 0

while balance > 0:
    month += 1
    interest = balance * (annual_interest_rate / 12)
    principal = monthly_payment - interest
    
    if balance < monthly_payment:
        principal = balance
        monthly_payment = interest + principal

    remaining_balance = balance - principal
    
    print(f"{month}\t${balance:,.2f}\t\t${interest:,.2f}\t\t${principal:,.2f}\t\t${monthly_payment:,.2f}\t\t${remaining_balance:,.2f}")
    
    balance = remaining_balance
