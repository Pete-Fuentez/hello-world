def main():
    number = float(input("Enter a number: "))
    result = square(number)
    print("The square of", number, "is", result)

def square(x):
    return x * x

if __name__ == "__main__":
    main()
