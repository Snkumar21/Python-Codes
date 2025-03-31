# Example of palindrome finder using user-defined function in python...

class PalindromeChecker:
    def __init__(self, num):
        self.num = num

    # main logic of the program
    def is_palindrome(self):
        return str(self.num) == str(self.num)[::-1]

# Input number
num = int(input("Enter a no.: "))

# Function calling
checker_obj = PalindromeChecker(num)

# Display the output
if checker_obj.is_palindrome():
    print(f"{num} is a Palindrome number.")
else:
    print(f"{num} is NOT a Palindrome number.")
