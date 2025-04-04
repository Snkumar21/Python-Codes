<<<<<<< HEAD
def create_tuple():
    """Creates a tuple based on user input."""
    elements = input("Enter tuple elements (comma-separated): ").split(',')
    return tuple(map(str.strip, elements))  # Remove whitespace


def display_tuple(tup):
    """Displays the tuple."""
    print(f"Tuple: {tup}\n")


def get_length(tup):
    """Returns the length of the tuple."""
    print(f"Length of tuple: {len(tup)}\n")


def get_max(tup):
    """Returns the maximum element of the tuple (numeric values only)."""
    try:
        print(f"Maximum element: {max(map(int, tup))}\n")
    except ValueError:
        print("Error: Tuple must contain only numeric values for max().\n")


def get_min(tup):
    """Returns the minimum element of the tuple (numeric values only)."""
    try:
        print(f"Minimum element: {min(map(int, tup))}\n")
    except ValueError:
        print("Error: Tuple must contain only numeric values for min().\n")


def get_sum(tup):
    """Returns the sum of elements (numeric values only)."""
    try:
        print(f"Sum of elements: {sum(map(int, tup))}\n")
    except ValueError:
        print("Error: Tuple must contain only numeric values for sum().\n")


def find_index(tup):
    """Finds the index of an element in the tuple."""
    element = input("Enter the element to find index: ").strip()
    if element in tup:
        print(f"Index of '{element}': {tup.index(element)}\n")
    else:
        print(f"'{element}' not found in tuple.\n")


def count_occurrences(tup):
    """Counts occurrences of an element in the tuple."""
    element = input("Enter the element to count: ").strip()
    print(f"'{element}' appears {tup.count(element)} times in the tuple.\n")


def sort_tuple(tup):
    """Sorts the tuple (returns a list since tuples are immutable)."""
    try:
        sorted_tuple = sorted(map(int, tup))
        print(f"Sorted tuple (as list): {sorted_tuple}\n")
    except ValueError:
        print("Error: Tuple must contain only numeric values for sorting.\n")


# Initial tuple
my_tuple = create_tuple()

# Menu-driven loop
while True:
    print("\nMENU:")
    print("1. Display Tuple")
    print("2. Length of Tuple")
    print("3. Maximum Element")
    print("4. Minimum Element")
    print("5. Sum of Elements")
    print("6. Find Index of an Element")
    print("7. Count Occurrences of an Element")
    print("8. Sort Tuple")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == '1':
        display_tuple(my_tuple)
    elif choice == '2':
        get_length(my_tuple)
    elif choice == '3':
        get_max(my_tuple)
    elif choice == '4':
        get_min(my_tuple)
    elif choice == '5':
        get_sum(my_tuple)
    elif choice == '6':
        find_index(my_tuple)
    elif choice == '7':
        count_occurrences(my_tuple)
    elif choice == '8':
        sort_tuple(my_tuple)
    elif choice == '9':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 9.\n")
=======
# This is a menu driven program of Tuple. All functions are used in this.

def create_tuple():
    elements = input("Enter tuple elements (comma-separated): ").split(',')
    return tuple(map(str.strip, elements))  # Remove whitespace


def display_tuple(tup):
    print(f"Tuple: {tup}\n")


def get_length(tup):
    print(f"Length of tuple: {len(tup)}\n")


def get_max(tup):
    try:
        print(f"Maximum element: {max(map(int, tup))}\n")
    except ValueError:
        print("Error: Tuple must contain only numeric values for max().\n")


def get_min(tup):
    try:
        print(f"Minimum element: {min(map(int, tup))}\n")
    except ValueError:
        print("Error: Tuple must contain only numeric values for min().\n")


def get_sum(tup):
    try:
        print(f"Sum of elements: {sum(map(int, tup))}\n")
    except ValueError:
        print("Error: Tuple must contain only numeric values for sum().\n")


def find_index(tup):
    element = input("Enter the element to find index: ").strip()
    if element in tup:
        print(f"Index of '{element}': {tup.index(element)}\n")
    else:
        print(f"'{element}' not found in tuple.\n")


def count_occurrences(tup):
    element = input("Enter the element to count: ").strip()
    print(f"'{element}' appears {tup.count(element)} times in the tuple.\n")


def sort_tuple(tup):
    try:
        sorted_tuple = sorted(map(int, tup))
        print(f"Sorted tuple (as list): {sorted_tuple}\n")
    except ValueError:
        print("Error: Tuple must contain only numeric values for sorting.\n")


# Initial tuple
my_tuple = create_tuple()

# Menu-driven loop
while True:
    print("\nMENU:")
    print("1. Display Tuple")
    print("2. Length of Tuple")
    print("3. Maximum Element")
    print("4. Minimum Element")
    print("5. Sum of Elements")
    print("6. Find Index of an Element")
    print("7. Count Occurrences of an Element")
    print("8. Sort Tuple")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == '1':
        display_tuple(my_tuple)
    elif choice == '2':
        get_length(my_tuple)
    elif choice == '3':
        get_max(my_tuple)
    elif choice == '4':
        get_min(my_tuple)
    elif choice == '5':
        get_sum(my_tuple)
    elif choice == '6':
        find_index(my_tuple)
    elif choice == '7':
        count_occurrences(my_tuple)
    elif choice == '8':
        sort_tuple(my_tuple)
    elif choice == '9':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 9.\n")
>>>>>>> 2f455337bbd98e35313ab1d5f2b408fa185fca51
