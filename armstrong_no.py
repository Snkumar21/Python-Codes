<<<<<<< HEAD
num = int(input("Enter a number: "))
order = len(str(num))
armstrong_sum = sum(int(digit) ** order for digit in str(num))

if num == armstrong_sum:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
=======
# Example of Armstrong Number using user-defined value.

# Input
num = int(input("Enter a number: "))
order = len(str(num))
armstrong_sum = sum(int(digit) ** order for digit in str(num))

# Display
if num == armstrong_sum:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
>>>>>>> 2f455337bbd98e35313ab1d5f2b408fa185fca51
