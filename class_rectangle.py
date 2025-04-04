<<<<<<< HEAD
# Write a program to implement a class named as rectangle, it has a method which computes the area and displays it?

class Rectangle:
    def __init__(self):
        self.length = 0
        self.breadth = 0
    def get(self):
        self.length = int(input("Enter length: "))
        self.breadth = int(input("Enter breadth: "))
    def area(self):
        return self.length * self.breadth
    def display(self):
        print("Area of rectangle: ", self.area())
r = Rectangle()
r.get()
r.display()
=======
# Write a program to implement a class named as rectangle, it has a method which computes the area and displays it?
# Example of rectangle area display using a class operator.

class Rectangle:
    def __init__(self):
        self.length = 0
        self.breadth = 0
    def get(self):
        self.length = int(input("Enter length: "))
        self.breadth = int(input("Enter breadth: "))
    def area(self):
        return self.length * self.breadth
    def display(self):
        print("Area of rectangle: ", self.area())
r = Rectangle()
r.get()
r.display()
>>>>>>> 2f455337bbd98e35313ab1d5f2b408fa185fca51
