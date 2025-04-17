# Example of List in python..

# Q1)
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(myList[::-1])

# Q2)
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
print(a + b)

# Q3)
ls = [20, 30, 40, 20, 50]
ls[0] = 10
print(ls)

# Q4)
course = ["Python", "Javascript", "DSA", "Software Project Management", "Coding toolkit", "Emerging technologies"]
course[5] = "Pre placement training"
print(course)

# Q5)
ls = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
ls = sum(ls)
print(ls)

# Q6)
# while(true):
#     if:
# elif:

# Q7)
x = [1, 2, 8, 4, 5, 2, 7, 8, 9, 10]
x = list(set(x)) # Convert list into set
print(x)

# Q8)
print("Even numbers between 1 to 100 are:")
for num in range(1, 101):
    if num % 2 == 0:
        print(num)

# Q9)
demo1 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(demo1[0:3])
print(demo1[1:9])
print(demo1[9])
demo1.sort(reverse = True)
print(demo1)

# Q10)
c = [10, 20, 30, 40, 50]
d = [30, 70, 10, 90, 100]
# Two ways for this question
e = list(set(c).intersection(set(d))) # Convert list into set
e = list(set(c) & (set(d)))
print(e)