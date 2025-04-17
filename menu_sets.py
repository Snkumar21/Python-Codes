# This is a menu driven program in sets.
def create_set():
    elements = input("Enter set elements (comma-separated): ").split(',')
    return set(map(str.strip, elements))  # Remove whitespace


def display_set(s):
    print(f"Set: {s}\n")


def add_element(s):
    element = input("Enter element to add: ").strip()
    s.add(element)
    print(f"Updated set: {s}\n")


def remove_element(s):
    element = input("Enter element to remove: ").strip()
    if element in s:
        s.remove(element)
        print(f"Updated set: {s}\n")
    else:
        print("Error: Element not found!\n")


def discard_element(s):
    element = input("Enter element to discard: ").strip()
    s.discard(element)
    print(f"Updated set: {s}\n")


def pop_element(s):
    if s:
        removed = s.pop()
        print(f"Removed element: {removed}")
        print(f"Updated set: {s}\n")
    else:
        print("Set is empty. Nothing to pop!\n")


def clear_set(s):
    s.clear()
    print("Set is now empty.\n")


def set_operations(s1, s2):
    print(f"\nFirst Set: {s1}")
    print(f"Second Set: {s2}")

    print(f"Union: {s1.union(s2)}")
    print(f"Intersection: {s1.intersection(s2)}")
    print(f"Difference (s1 - s2): {s1.difference(s2)}")
    print(f"Symmetric Difference: {s1.symmetric_difference(s2)}")

    print(f"Is s1 a subset of s2? {s1.issubset(s2)}")
    print(f"Is s1 a superset of s2? {s1.issuperset(s2)}\n")


# Initial set
my_set = create_set()

# Menu-driven loop
while True:
    print("\nMENU:")
    print("1. Display Set")
    print("2. Add Element")
    print("3. Remove Element")
    print("4. Discard Element")
    print("5. Pop Element")
    print("6. Clear Set")
    print("7. Set Operations (Union, Intersection, Difference, etc.)")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        display_set(my_set)
    elif choice == '2':
        add_element(my_set)
    elif choice == '3':
        remove_element(my_set)
    elif choice == '4':
        discard_element(my_set)
    elif choice == '5':
        pop_element(my_set)
    elif choice == '6':
        clear_set(my_set)
    elif choice == '7':
        second_set = create_set()
        set_operations(my_set, second_set)
    elif choice == '8':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 8.\n")