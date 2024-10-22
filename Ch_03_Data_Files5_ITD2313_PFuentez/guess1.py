import math

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))

max_guesses = math.ceil(math.log2(larger - smaller + 1))
print(f"I will guess your number in at most {max_guesses} tries!")

count = 0
low = smaller
high = larger

while count < max_guesses:
    count += 1
    guess = (low + high) // 2
    print(f"My guess is {guess}")
    
    feedback = int(input("Enter '1' for correct, '2' for too small, '3' for too large: "))
    
    if feedback == 1:
        print(f"I've got it in {count} tries!")
        break
    elif feedback == 2:
        low = guess + 1
    elif feedback == 3:
        high = guess - 1
    else:
        print("Invalid input. Please enter '1', '2', or '3'.")

if count == max_guesses and feedback != 1:
    print("Something went wrong. Are you sure you gave the correct hints?")
