class Parent():
    z=30
    def __init__(self):
        print("In Constructor")
        self.x=10
        self.y=30

    def dispData(self):
        print(self.x)
        print(self.y)
    @classmethod
    def dispParent(cls):
        print(cls.z)

    def __del__(self):
        print("In destructor")


#type-1
# obj=Parent()
# obj.dispData()
# obj.dispParent()
# # obj.__del__()
# del obj



# type-2
obj=Parent()
obj=Parent()
print("game Over")
