def read_file_line_by_line(filename):
    try:
        with open(filename, 'r') as file:
            print("File Contents:\n")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found.")

# Example usage:
read_file_line_by_line("demotextfile.txt")