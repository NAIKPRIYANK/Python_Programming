class Parent:
    def __init__(self):
        print("In Parent")

    def parentFunc(self):
        print("In parent fun")
class child(Parent):
    pass

obj1=Parent()
obj1.parentFunc()