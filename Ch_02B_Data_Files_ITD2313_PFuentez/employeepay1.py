hourly_wage = float(input("Enter the hourly wage: "))
regular_hours = float(input("Enter the total number of regular hours: "))
overtime_hours = float(input("Enter the total number of overtime hours: "))

regular_pay = hourly_wage * regular_hours
overtime_pay = overtime_hours * hourly_wage * 1.5
total_pay = regular_pay + overtime_pay

print("The total weekly pay is:", total_pay)
