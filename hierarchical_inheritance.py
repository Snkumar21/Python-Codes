# Example of Hierarchical

class Parent:
    def parentfunc(self):
        print("This function belongs to parent")

class Child1(Parent):
    def childfunc1(self):
        print("This function belongs to child 1")
class Child2(Parent):
    def childfunc2(self):
        print("This function belongs to child 2")

child1ob = Child1()
child1ob.parentfunc()
child1ob.childfunc1()
child2ob = Child2()
child2ob.parentfunc()
child2ob.childfunc2()