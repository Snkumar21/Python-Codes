# Example of python program to implement class, object, user defined function to display reverse of a number...

class Reverse:
    def __init__(self, num):
        self.num = num

    def reverse(self):
        rev = 0
        while self.num > 0:
            rem = self.num % 10
            rev = rev * 10 + rem
            self.num = self.num // 10
        return rev
    
num = int(input("Enter a number: "))
obj = Reverse(num)
print("Reverse of", num, "is", obj.reverse())