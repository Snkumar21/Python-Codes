<<<<<<< HEAD
# Write python program to implement class, object, user defined function to check whether the number is palindrome or not?

class Palindrome:
    def __init__(self, num):
        self.num = num

    def palindrome(self):
        temp = self.num
        rev = 0
        while self.num > 0:
            rem = self.num % 10
            rev = rev * 10 + rem
            self.num = self.num // 10
        if temp == rev:
            return True
        else:
            return False
        
num = int(input("Enter a number: "))
obj = Palindrome(num)
if obj.palindrome():
    print(num, "is palindrome")
else:
    print(num, "is not palindrome")
=======
# Example of python program to implement class, object, user defined function to check whether the number is palindrome or not...

class Palindrome:
    def __init__(self, num):
        self.num = num

    def palindrome(self):
        temp = self.num
        rev = 0
        while self.num > 0:
            rem = self.num % 10
            rev = rev * 10 + rem
            self.num = self.num // 10
        if temp == rev:
            return True
        else:
            return False
        
num = int(input("Enter a number: "))
obj = Palindrome(num)
if obj.palindrome():
    print(num, "is palindrome")
else:
    print(num, "is not palindrome")
>>>>>>> 2f455337bbd98e35313ab1d5f2b408fa185fca51
