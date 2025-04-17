# Example of Hierarchical Inheritance using pre-defined value.

# Parent Class
class Parent:
    def parentfunc(self):
        print("This function belongs to parent")

# Child1 Class
class Child1(Parent):
    def childfunc1(self):
        print("This function belongs to child 1")

# Child2 Class
class Child2(Parent):
    def childfunc2(self):
        print("This function belongs to child 2")

# Calling the classes
child1ob = Child1()
child1ob.parentfunc()
child1ob.childfunc1()
child2ob = Child2()
child2ob.parentfunc()
child2ob.childfunc2()