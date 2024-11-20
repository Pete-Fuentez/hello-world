"""
Program: minutes.py
Author: Pete Fuentez

This program uses the following steps:

1. Defines constants for the number of minutes per hour, hours per day, and days per year.
2. Request the input number of years.
3. Compute the number of minutes. The total number of minutes multiplying the number of years by the number of days per year, hours per day, and minutes per hour.
4. display the result.
"""
# Constants
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
DAYS_PER_YEAR = 365

# Request the input
years = int(input("Enter the number of years: "))

# Compute the number of minutes
minutes = years * DAYS_PER_YEAR * HOURS_PER_DAY * MINUTES_PER_HOUR

# Display the result
print(f"The number of minutes in {years} years is {minutes}.")

