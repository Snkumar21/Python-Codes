#This is Grade System Calculator in Python Language.
sub1 = int(input("Enter marks for subject 1: \n"))
sub2 = int(input("Enter marks for subject 2: \n"))
sub3 = int(input("Enter marks for subject 3: \n"))
sub4 = int(input("Enter marks for subject 4: \n"))
sub5 = int(input("Enter marks for subject 5: \n"))

total_marks = sub1+sub2+sub3+sub4+sub5
average_marks = total_marks/5

if average_marks >= 80:
    print("The grade of the student is: A")
elif average_marks >= 70:
    print("The grade of the student is: B")
elif average_marks >= 50:
    print("The grade of the student is: C")
elif average_marks >= 40:
    print("The grade of the student is: D")
else:
    print("The grade of the student is: F")
