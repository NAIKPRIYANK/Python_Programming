class Parent():
    def __init__(self):
        print("In Constructor")
        self.x=10
        self.y=30
    def dispData(self):
        print(self.x)
        print(self.y)
class Child(Parent):
    def __init__(self):
        # super().__init__()
        print("In Child Constructor")
        self.x=30
        self.y=40
        super().__init__() 
obj=Child()
obj.dispData()
        

    