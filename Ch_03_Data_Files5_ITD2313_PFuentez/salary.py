starting_salary = float(input("Enter the starting salary: "))
percentage_increase = float(input("Enter the percentage increase (e.g., enter 2 for 2%): "))
years = int(input("Enter the number of years in the schedule: "))

print("\nYear\tSalary")
print("----------------------")

current_salary = starting_salary
for year in range(1, years + 1):
    print(f"{year}\t${current_salary:,.2f}")
    current_salary += current_salary * (percentage_increase / 100)
