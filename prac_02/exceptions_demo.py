try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers.txt!")
print("Finished.")

# A ValueError will occur whenever the user inputs a non-integer
# A ZeroDivisionError will occur whenever the user inputs "0"
# A ZeroDivisionError can be avoided by adding a while loop that asks the user to enter a denominator that is not 0
