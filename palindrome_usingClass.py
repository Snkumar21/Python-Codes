class Palindrome:
    def __init__(self, num):
        self.num = num

    def is_palindrome(self):
        return str(self.num) == str(self.num)[::-1]

# Example usage
num = int(input("Enter a number: "))
pal = Palindrome(num)
if pal.is_palindrome():
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")