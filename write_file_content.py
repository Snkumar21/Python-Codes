file2 = open("demotextfile.txt", "w")

file2.write("Hello, this is nitish...\n")
file2.write("Welcome to the world")

file2 = open("demotextfile.txt")
readfile = file2.read()
print(readfile)