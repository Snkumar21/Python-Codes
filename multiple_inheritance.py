<<<<<<< HEAD
#Multiple Inheritance
class Parent1:
    def parentfunc1(self):
        print("This function belongs to parent1")

class Parent2:
    def parentfunct2(self):
        print("This function belongs to parent 2")

class Child1(Parent1,Parent2):
    def childfunc(self):
        print("This function belongs to child")

ch1=Child1()
ch1.parentfunc1()
ch1.parentfunct2()
ch1.childfunc()
=======
# Multiple Inheritance in python.

class Parent1:
    def parentfunc1(self):
        print("This function belongs to parent1")

class Parent2:
    def parentfunct2(self):
        print("This function belongs to parent 2")

class Child1(Parent1,Parent2):
    def childfunc(self):
        print("This function belongs to child")

ch1=Child1()
ch1.parentfunc1()
ch1.parentfunct2()
ch1.childfunc()
>>>>>>> 2f455337bbd98e35313ab1d5f2b408fa185fca51
