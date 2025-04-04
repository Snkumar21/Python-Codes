def divide_string(s, n):
    length = len(s)
    if length % n != 0:
        return "String cannot be divided into equal parts."
    
    part_size = length // n
    parts = [s[i:i + part_size] for i in range(0, length, part_size)]
    
    return parts

string = input("Enter a string: ")
num_parts = int(input("Enter the number of equal parts: "))

result = divide_string(string, num_parts)

print("Divided parts:", result)