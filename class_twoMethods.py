# Write a program to implement a class which has at least two methods i.e. to input the string from the user and display it in upper case?

class String:
    def __init__(self):
        self.str = ""
    def get(self):
        self.str = input("Enter a string: ")
    def display(self):
        print("String in upper case: ", self.str.upper())
s = String()
s.get()
s.display()