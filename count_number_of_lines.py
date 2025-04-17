# Example of count number of lines in python...
def count_lines_not_starting_with_T(filename):
    count = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                if not line.strip().startswith('T'):
                    count += 1
        print(f"Lines not starting with 'T': {count}")
    except FileNotFoundError:
        print("File not found.")

# Example usage:
count_lines_not_starting_with_T("demotextfile.txt")