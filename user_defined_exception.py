# User-defined exceptions
class InvalidAgeException(Exception):
    "Raised when the age is less than 18"
    pass
age = 18
try:
    input_age = int(input("Enter a age: "))
    if input_age < age:
        raise InvalidAgeException
    else:
        print("You can vote")
    
except InvalidAgeException:
    print("Invalid Age")