class parent:
    def parentFun(self):
        print("Parent class function")

class child(parent):
    def childFun(self):
        print("Child class function")
        
ch = child()
ch.parentFun()
ch.childFun()