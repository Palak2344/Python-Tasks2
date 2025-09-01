# Function to check if a number is even or odd
def check_even_odd():
    # Taking an integer input from the user
    number = int(input("Enter an integer: "))

    # Checking if the number is even or odd using an if-else statement
    if number % 2 == 0:
        result = "even"
    else:
        result = "odd"

    # Displaying the result
    print(f"The number {number} is {result}.")

# Calling the function to execute the program
check_even_odd()
