def add_numbers(num1, num2):
    return num1 + num2

# Main program
def main():
    # Asking for input
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    # Calculating the sum
    sum = add_numbers(number1, number2)

    # Displaying the result
    print(f"The sum of {number1} and {number2} is {sum}")

# Executing the main program
if __name__ == "__main__":
    main()