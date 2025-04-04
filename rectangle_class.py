<<<<<<< HEAD
# This is a rectangle class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area_display(self):
        return self.length * self.width

    def display(self):
        print("Area of the Rectangle :", self.area_display())

# Enter the input
length = int(input("Enter a Length: "))
width = int(input("Enter a Width: "))

string_obj = Rectangle(length, width)

string_obj.display()
=======
# Example of rectangle class in python...

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area_display(self):
        return self.length * self.width

    def display(self):
        print("Area of the Rectangle :", self.area_display())

# Enter the input
length = int(input("Enter a Length: "))
width = int(input("Enter a Width: "))

string_obj = Rectangle(length, width)

string_obj.display()
>>>>>>> 2f455337bbd98e35313ab1d5f2b408fa185fca51
