class StringManipulator:
    def __init__(self):
        self.text = " "

    def input_string(self):
        self.text = input("Enter a string: ")

    def display_uppercase(self):
        print("Uppercase String:", self.text.upper())

string_obj = StringManipulator()

string_obj.input_string()
string_obj.display_uppercase()