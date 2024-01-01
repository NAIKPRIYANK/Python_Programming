class Parent:
    z=40
    def __init__(self) -> None:
        print("In Parent Constructor")
        self.x=10
        self.y=20

    def dispData(self):
        print(self.x)
        print(self.y)

    @classmethod
    def dispclassm(cal):
        print(cal.z);
        print("hello in class method")
        print(Parent.z)

    @staticmethod
    def dispStatic():
        print("in static method")
        print(Parent.z)

class Child(Parent):
    pass


obj1=Parent()
obj1.dispStatic()
obj=Child()
obj.dispData()
obj.dispclassm()
obj.dispStatic()

