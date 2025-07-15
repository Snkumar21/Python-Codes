# Read 5 space-separated integers
numbers = list(map(int, input().strip().split()))

# Check that exactly 5 numbers are entered
if len(numbers) != 5:
    print("Error: Please enter exactly 5 numbers.")
else:
    # Print the largest number
    print(max(numbers))