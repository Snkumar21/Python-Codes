# Dictionary to store student records (name as key, grades as values)
students = {}

def add_student():
    name = input("Enter student name: ")
    grades = input("Enter student grades (comma-separated): ").split(',')
    students[name] = [int(grade.strip()) for grade in grades]
    print(f"Student '{name}' added successfully!\n")

def remove_student():
    name = input("Enter student name to remove: ")
    if name in students:
        del students[name]
        print(f"Student '{name}' removed successfully!\n")
    else:
        print(f"Student '{name}' not found!\n")

def print_grades():
    name = input("Enter student name to print grades: ")
    if name in students:
        print(f"{name}'s Grades: {students[name]}\n")
    else:
        print(f"Student '{name}' not found!\n")

def print_menu():
    print("\nMENU:")
    print("1. Add a Student")
    print("2. Remove a Student")
    print("3. Print Grades of a Student")
    print("4. Print Menu")
    print("5. Exit\n")

# Display the menu initially
print_menu()

# Main loop for user interaction
while True:
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        remove_student()
    elif choice == '3':
        print_grades()
    elif choice == '4':
        print_menu()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.\n")