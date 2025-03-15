
class Parent:
    def parentFunc(self):
        print("Parent Function")
class Child(Parent):
    def childFunc(self):
        print("Child Function")
ch = Child()    
ch.parentFunc()
ch.childFunc()