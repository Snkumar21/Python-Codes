# Example of write a file content in python...

# Open the file in write mode
file2 = open("demotextfile.txt", "w")

# Write the content to the file
file2.write("Hello, this is nitish...\n")
file2.write("Welcome to the world")

# Re-opening the file in read mode to read the content
file2 = open("demotextfile.txt")
readfile = file2.read()

# Print the content of the file
print(readfile)