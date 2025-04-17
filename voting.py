# Program to check whether a person is eligible to vote or not

num = int(input("Enter the age: "))
if num >= 18:
    print("Eligible to vote")
elif num < 18:
    print("Not eligible to vote")