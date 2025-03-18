# Different ways to generate strings in Python

# 1. Basic string creation
simple_string = "Hello, World!"
print("Simple string:", simple_string)

# 2. String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Concatenated string:", full_name)

# 3. String formatting using f-strings (Python 3.6+)
age = 25
formatted_string = f"My name is {full_name} and I am {age} years old"
print("Formatted string:", formatted_string)

# 4. String multiplication
repeated_string = "Python! " * 3
print("Repeated string:", repeated_string)

# 5. String with special characters
special_string = "Line 1\nLine 2\tTabbed text"
print("String with special characters:")
print(special_string)

# 6. String methods
string_methods = "Python Programming"
print("String methods:", string_methods)
print("Uppercase:", string_methods.upper())
print("Lowercase:", string_methods.lower())

# 7. String slicing
substring = "Hello, World!"
print("Substring:", substring[0:5])

# 8. String interpolation
name = "Alice"
age = 30
greeting = f"Hello, {name}! You are {age} years old."
print("Interpolated string:", greeting)

# 9. String formatting with format()
template = "Hello, {name}! You are {age} years old."
formatted_string = template.format(name="Bob", age=45)
print("Formatted string:", formatted_string)

# 10. String formatting with % operator
name = "Charlie"
age = 28
formatted_string = "Name: %s, Age: %d" % (name, age)
print("Formatted string:", formatted_string)

# 11. String formatting with format() using dictionary
data = {"name": "David", "age": 35}
formatted_string = "Name: {name}, Age: {age}".format(**data)
print("Formatted string:", formatted_string)

# 12. String formatting with format() using positional arguments
formatted_string = "Name: {1}, Age: {0}".format(age, name)
print("Formatted string:", formatted_string)

# 13. String formatting with format() using keyword arguments
formatted_string = "Name: {name}, Age: {age}".format(name="Eve", age=22)
print("Formatted string:", formatted_string)

# 14. String formatting with format() using padding and alignment
formatted_string = "Name: {:<10}, Age: {:*^10}".format(name, age)
print("Formatted string:", formatted_string)

# 15. String formatting with format() using padding and alignment
formatted_string = "Name: {:*^10}, Age: {:*^10}".format(name, age)
print("Formatted string:", formatted_string)