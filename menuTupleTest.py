<<<<<<< HEAD
# Write menu driven python program to implement at least 5 built-in functions of tuple.

def displayMenu():
    print("\nMenu:")
    print("1. Length of tuple")
    print("2. Maximum value")
    print("3. Minimum value")
    print("4. Count occurrences of an element")
    print("5. Convert tuple to list")
    print("6. Exit")

myTuple = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

while True:
    displayMenu()
    choice = input("Select menu from (1-7): ")

    if choice == "1":
        print("Length of Tuple:", len(myTuple))

    elif choice == "2":
        print("Maximum value in tuple:", max(myTuple))

    elif choice == "3":
        print("Minimum value in tuple:", min(myTuple))

    elif choice == "4":
        element = int(input("Enter element to count: "))
        print(f"Occurrences of {element}: {myTuple.count(element)}")

    elif choice == "5":
        tupleToList = list(myTuple)
        print("Tuple converted to list:", tupleToList)

    elif choice == "6":
        print("Exit")
        break

    else:
        print("Incorrect choice, please enter a number between 1 and 7.")

=======
# Example of menu driven python program to implement at least 5 built-in functions of tuple.

def displayMenu():
    print("\nMenu:")
    print("1. Length of tuple")
    print("2. Maximum value")
    print("3. Minimum value")
    print("4. Count occurrences of an element")
    print("5. Convert tuple to list")
    print("6. Exit")

myTuple = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

while True:
    displayMenu()
    choice = input("Select menu from (1-7): ")

    if choice == "1":
        print("Length of Tuple:", len(myTuple))

    elif choice == "2":
        print("Maximum value in tuple:", max(myTuple))

    elif choice == "3":
        print("Minimum value in tuple:", min(myTuple))

    elif choice == "4":
        element = int(input("Enter element to count: "))
        print(f"Occurrences of {element}: {myTuple.count(element)}")

    elif choice == "5":
        tupleToList = list(myTuple)
        print("Tuple converted to list:", tupleToList)

    elif choice == "6":
        print("Exit")
        break

    else:
        print("Incorrect choice, please enter a number between 1 and 7.")

>>>>>>> 2f455337bbd98e35313ab1d5f2b408fa185fca51
