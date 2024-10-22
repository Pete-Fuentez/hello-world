"""
Program: minutes.py
Author: Pete Fuentez

This program follows these steps:

1. Request the inputs takes the hourly wage, total regular hours, and total overtime hours as inputs.
2. Compute the total weekly pay take the regular pay by multiplying the hourly wage by the total regular hours.
3. Compute the overtime pay by multiplying the total overtime hours by 1.5 times the hourly wage.
4. Adds the regular pay and overtime pay to get the total weekly pay.
5. Displays the total weekly pay, formatted to two decimal places.
"""

# Request the inputs
hourlyWage = float(input("Enter the hourly wage: "))
regularHours = float(input("Enter the total number of regular hours: "))
overtimeHours = float(input("Enter the total number of overtime hours: "))

# Compute the total weekly pay
regularPay = hourlyWage * regularHours
overtimePay = overtimeHours * hourlyWage * 1.5
totalPay = regularPay + overtimePay

# Display the total weekly pay
print(f"The total weekly pay is ${totalPay:.2f}")
