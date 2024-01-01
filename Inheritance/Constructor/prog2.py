class Parent:
    def __init__(self) -> None:
        print("In Parent constructor ")
    def parentFun(self):
        print("In Parent fun")

class Child(Parent):
    def __init__(self) -> None:
        print("In child constructor")

obj1=Child()
obj1.parentFun()



