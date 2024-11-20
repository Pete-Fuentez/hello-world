# Function to calculate the total distance traveled by the ball
def calculate_total_distance(initial_height, bounciness_index, num_bounces):
    total_distance = 0
    height = initial_height

    # Loop through each bounce
    for i in range(num_bounces):
        # The ball travels down and up, so add the fall and the bounce
        total_distance += height  # fall
        height *= bounciness_index  # height after bounce
        total_distance += height  # bounce back up

    return total_distance

# Main program
def main():
    try:
        # Input: initial height, bounciness index, and number of bounces
        initial_height = float(input("Enter the initial height : "))
        bounciness_index = float(input("Enter the bounciness index : "))
        num_bounces = int(input("Enter the number of bounces: "))

        # Calculate total distance
        total_distance = calculate_total_distance(initial_height, bounciness_index, num_bounces)

        # Output the total distance traveled
        print(f"The total distance traveled by the ball is {total_distance:.2f} feet.")

    except ValueError:
        print("Please enter valid numerical values.")

# Run the program
if __name__ == "__main__":
    main()
