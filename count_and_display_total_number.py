# Example of count and display total number...

def count_total_words(filename):
    total_words = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()
                total_words += len(words)
        print(f"Total number of words: {total_words}")
    except FileNotFoundError:
        print("File not found.")

# Example usage:
count_total_words("demotextfile.txt")