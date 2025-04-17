# Enter the week day from the user based on the day display the day of the week in words

number = int(input("Enter a day number:-  "))
if number == 1:
    print("Monday")
elif number == 2:
    print("Tuesday")
elif number == 3:
    print("Wednesday")
elif number == 4:
    print("Thursday")
elif number == 5:
    print("Friday")
elif number == 6:
    print("Saturday")
elif number == 7:
    print("Sunday")
else:
    print("Invalid input, please enter a number between 1 and 7.")