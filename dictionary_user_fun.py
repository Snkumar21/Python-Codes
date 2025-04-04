<<<<<<< HEAD
# Class to find square roots using a dictionary
class Square:
    def __init__(self, square_dict):
        self.square_dict = square_dict  # Store the dictionary

    # Method to find square roots
    def display_squares(self):
        print("Number\tSquare")
        for num, sq in self.square_dict.items():
            print(f"{num} \t {sq}")

# Dictionary containing numbers and their squares
square_dict = {
    1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100,
    11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256, 17: 289, 18: 324, 19: 361, 20: 400,
    21: 441, 22: 484, 23: 529, 24: 576, 25: 625, 26: 676, 28: 784, 29: 841, 30: 900
}

# Creating an object of Square class
checker_obj = Square(square_dict)

# Display the output
checker_obj.display_squares()
=======
# Example of dictionary in python.

# Class to find square roots using a dictionary
class Square:
    def __init__(self, square_dict):
        self.square_dict = square_dict  # Store the dictionary

    # Method to find square roots
    def display_squares(self):
        print("Number\tSquare")
        for num, sq in self.square_dict.items():
            print(f"{num} \t {sq}")

# Dictionary containing numbers and their squares
square_dict = {
    1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100,
    11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256, 17: 289, 18: 324, 19: 361, 20: 400,
    21: 441, 22: 484, 23: 529, 24: 576, 25: 625, 26: 676, 28: 784, 29: 841, 30: 900
}

# Creating an object of Square class
checker_obj = Square(square_dict)

# Display the output
checker_obj.display_squares()
>>>>>>> 2f455337bbd98e35313ab1d5f2b408fa185fca51
