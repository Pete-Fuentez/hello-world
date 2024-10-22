# navigate.py

def main():
    # Prompt for the filename
    filename = input("Enter the filename: ")

    try:
        # Read the file and store lines in a list
        with open(filename, 'r') as file:
            lines = file.readlines()

        num_lines = len(lines)
        print(f"Number of lines in the file: {num_lines}")

        while True:
            # Prompt user for a line number
            line_number = int(input(f"Enter a line number (1-{num_lines}) or 0 to quit: "))

            if line_number == 0:
                print("Exiting the program.")
                break

            # Check if the line number is valid
            if 1 <= line_number <= num_lines:
                # Print the corresponding line
                print(f"Line {line_number}: {lines[line_number - 1].strip()}")
            else:
                print("Invalid line number. Please try again.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError:
        print("Invalid input. Please enter a valid line number.")

if __name__ == "__main__":
    main()
