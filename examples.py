# Example of multiple codes execution in a single program in python.
no = 3
if no < 5: # Conditional checking...
    print("The number is less than 5")

setflag = True
if setflag:
    print("Good Morning!")
    print("Solve the assignment")
setflag = False
if setflag:
    print("Good Afternoon!")
    print("Solve the assignment")   
print("Execute false") # Irrespective of the condition, this statement will be executed
