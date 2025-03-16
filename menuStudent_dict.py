def display_menu():
    print("\nMenu:")
    print("1. Add a student")
    print("2. Remove a student")
    print("3. Print grades of the students")
    print("4. Print the menu")
    print("5. Exit")

def main():
    students = {}  # Dictionary to store student names and their grades
    display_menu()

    while True:
        choice = int(input("\nEnter your choice (1-5): "))
        
        if choice == 1:
            # Add a student
            name = input("Enter the student's name: ")
            grade = input("Enter the student's grade: ")
            students[name] = grade
            print(f"Student '{name}' with grade '{grade}' added.")

        elif choice == 2:
            # Remove a student
            name = input("Enter the student's name to remove: ")
            if name in students:
                del students[name]
                print(f"Student '{name}' removed.")
            else:
                print(f"Student '{name}' not found.")

        elif choice == 3:
            # Print grades of the students
            if students:
                print("\nStudents and their grades:")
                for name, grade in students.items():
                    print(f"{name}: {grade}")
            else:
                print("No students found.")

        elif choice == 4:
            # Print the menu
            display_menu()

        elif choice == 5:
            # Exit the program
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
