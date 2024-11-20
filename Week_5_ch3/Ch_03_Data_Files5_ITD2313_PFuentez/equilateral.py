# Function to check if the triangle is equilateral
def is_equilateral(a, b, c):
    # In an equilateral triangle, all three sides are equal
    if a == b == c:
        return True
    else:
        return False

# Main program
def main():
    # Input: lengths of the three sides
    try:
        a = float(input("Enter the length of the first side: "))
        b = float(input("Enter the length of the second side: "))
        c = float(input("Enter the length of the third side: "))
    
        # Check if the triangle is equilateral
        if is_equilateral(a, b, c):
            print("The triangle is an equilateral triangle.")
        else:
            print("The triangle is not an equilateral triangle.")
    
    except ValueError:
        print("Please enter valid numbers for the side lengths.")

# Run the program
if __name__ == "__main__":
    main()
