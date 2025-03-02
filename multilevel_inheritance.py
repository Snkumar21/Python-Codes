# Example of Multilevel Inheritance

class Parent:
    def parentfunct(self):
        print("This function belongs to parent ")

class Child1(Parent):
    def childfunc1(self):
        print("This function belongs to child 1")

class Child2(Child1):
    def childfunc2(self):
        print("This function belongs to child 2")

child2ob = Child2()
child2ob.parentfunct()
child2ob.childfunc1()
child2ob.childfunc2()