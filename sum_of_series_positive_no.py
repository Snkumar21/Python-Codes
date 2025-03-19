# Initialize variables
total_sum = 0

print("Enter positive numbers to calculate their sum.")
print("To stop and see the result, enter a negative number.")

while True:
    try:
        # Take input from the user
        num = float(input("Enter a number: "))
        
        # Check if the number is negative
        if num < 0:
            print("Negative number entered. Stopping the input process.")
            break  # Exit the loop
        
        # Add the number to the total sum
        total_sum += num
    except ValueError:
        # Handle invalid input gracefully
        print("Invalid input. Please enter a valid number.")

# Display the final result
print(f"The sum of the entered positive numbers is: {total_sum}")