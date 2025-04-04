<<<<<<< HEAD
# str = "  Nitish"
# reversed_s = " "
# for char in str:
#     reversed_s = char + reversed_s

# for char in str:
#     reversed_s = reversed_s + char
# print(reversed_s)

def reverse_string(s):
    trimmed_str = s.strip()
    reversed_str = trimmed_str[::-1]
    return reversed_str

input_str = "  Hello World  "
print("Original String: '{}'".format(input_str))
print("Trimmed String: '{}'".format(input_str.strip()))
=======
# str = "  Nitish"
# reversed_s = " "
# for char in str:
#     reversed_s = char + reversed_s

# for char in str:
#     reversed_s = reversed_s + char
# print(reversed_s)

def reverse_string(s):
    trimmed_str = s.strip()
    reversed_str = trimmed_str[::-1]
    return reversed_str

input_str = "  Hello World  "
print("Original String: '{}'".format(input_str))
print("Trimmed String: '{}'".format(input_str.strip()))
>>>>>>> 2f455337bbd98e35313ab1d5f2b408fa185fca51
print("Reversed String: '{}'".format(reverse_string(input_str)))