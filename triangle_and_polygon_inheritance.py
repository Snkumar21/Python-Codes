class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides

    def display_sides(self):
        print(f"The polygon has {self.num_sides} sides.")

# Derived class inheriting from Polygon
class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__(3)
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def display_area(self):
        print(f"The area of the triangle is: {self.calculate_area()} square units.")

# Taking user input for base and height
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Creating an object of Triangle
triangle_obj = Triangle(base, height)

# Displaying
triangle_obj.display_sides()
triangle_obj.display_area()
