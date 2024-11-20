def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        return [float(line.strip()) for line in file if line.strip().isdigit() or line.strip().replace('.', '', 1).isdigit()]

def compute_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    filename = input("Enter the filename containing numbers: ")
    numbers = read_numbers_from_file(filename)
    average = compute_average(numbers)
    print(f"The average of the numbers in the file is: {average}")

if __name__ == "__main__":
    main()
