<<<<<<< HEAD
class NumberReverser:
    def __init__(self, num):
        self.num = num

    def reverse_number(self):
        rev_num = int(str(self.num)[::-1])
        return rev_num

num = int(input("Enter a number: "))

reverser_obj = NumberReverser(num)

print(f"The reverse of {num} is: {reverser_obj.reverse_number()}")
=======
# Example of reverse a number using user-defined function in python...

class NumberReverser:
    def __init__(self, num):
        self.num = num

    def reverse_number(self):
        rev_num = int(str(self.num)[::-1])
        return rev_num

num = int(input("Enter a number: "))

reverser_obj = NumberReverser(num)

print(f"The reverse of {num} is: {reverser_obj.reverse_number()}")
>>>>>>> 2f455337bbd98e35313ab1d5f2b408fa185fca51
