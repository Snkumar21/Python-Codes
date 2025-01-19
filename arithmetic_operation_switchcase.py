#Arithmetic Operations using Switch Case in python.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

while True:
    print("Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    # Get the user's choice
    choice = input("Enter choice (1/2/3/4/5):\n")

    if choice == '5':  # Exit condition
        print("Exiting program.")
        break

    # Validate the choice
    if choice in ['1', '2', '3', '4']:
        # Get two numbers from the user
        num1 = float(input("Enter first number:\n"))
        num2 = float(input("Enter second number:\n"))

        # Perform the operation based on the user's choice
        if choice == '1':
            print("Result:", add(num1, num2),"\n")
        elif choice == '2':
            print("Result:", subtract(num1, num2),"\n")
        elif choice == '3':
            print("Result:", multiply(num1, num2),"\n")
        elif choice == '4':
            print("Result:", divide(num1, num2),"\n")
    else:
        print("Invalid choice! Please select a valid option.")
