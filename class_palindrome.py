<<<<<<< HEAD
# Create a class, create user defined method to check whether a string is palindrome or not?

class Palindrome:
    def __init__(self, str):
        self.str = str
    def isPalindrome(self):
        start = 0
        end = len(self.str) - 1

        while start <= end:
            if self.str[start] != self.str[end]:
                return False
            start += 1
            end -= 1
        return True
str = input("Enter the string: ")
pal = Palindrome(str)
print(pal.isPalindrome())
=======
# Create a class, create user defined method to check whether a string is palindrome or not?
# Example of palindrome using a class operator.

class Palindrome:
    def __init__(self, str):
        self.str = str
    def isPalindrome(self):
        start = 0
        end = len(self.str) - 1

        while start <= end:
            if self.str[start] != self.str[end]:
                return False
            start += 1
            end -= 1
        return True
str = input("Enter the string: ")
pal = Palindrome(str)
print(pal.isPalindrome())
>>>>>>> 2f455337bbd98e35313ab1d5f2b408fa185fca51
