# Function to calculate the sum of integers from 1 to 50
def sum_of_integers():
    total_sum = 0  # Initialize the sum variable

    # Using a for loop to iterate over numbers from 1 to 50
    for number in range(1, 51):
        total_sum += number  # Add each number to the total sum

    # Displaying the final sum
    print(f"The sum of integers from 1 to 50 is: {total_sum}")

# Calling the function to execute the program
sum_of_integers()
