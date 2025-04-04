<<<<<<< HEAD
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
=======
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
>>>>>>> 2f455337bbd98e35313ab1d5f2b408fa185fca51
    print("Invalid Age")