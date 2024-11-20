# Function to calculate population growth
def predict_population(initial_population, growth_rate, growth_period, total_hours):
    # Calculate the number of growth periods
    num_growth_periods = total_hours // growth_period
    
    # Calculate the final population
    final_population = initial_population * (growth_rate ** num_growth_periods)
    
    return final_population

# Main program
def main():
    try:
        # Input: initial population, growth rate, growth period, and total hours
        initial_population = int(input("Enter the initial number of organisms: "))
        growth_rate = float(input("Enter the rate of growth (e.g., 2 for doubling): "))
        growth_period = int(input("Enter the number of hours to achieve this growth rate: "))
        total_hours = int(input("Enter the total number of hours for population growth: "))

        # Predict the total population
        final_population = predict_population(initial_population, growth_rate, growth_period, total_hours)

        # Output the predicted population
        print(f"The total population after {total_hours} hours will be {int(final_population)} organisms.")

    except ValueError:
        print("Please enter valid numbers for all inputs.")

# Run the program
if __name__ == "__main__":
    main()
