class Parent:
    def __init__(self) -> None:
        print("In Parent constructor ")
    def parentFun(self):
        print("In Parent fun")

class Child(Parent):
    def __init__(self) -> None:
        # Parent() Parent object is created so its not efficient in space
        # Parent.__init__(self) 
        # super().__init__()
        print(id(Parent.__init__(self)))
        print(id(super().__init__()))
        # super.__init__(self)Error

        print("In child constructor")

    def childFun(self):
        print("In Child fun")


obj1=Child()
obj1.parentFun()
obj1.childFun()
