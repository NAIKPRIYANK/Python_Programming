class Demo:
    def __init__(self) -> None:
        print("in Constructor")
    def __del__(self):
        print("In Destructor")

# type-1
# obj1=Demo()
# obj2=Demo()

#type-2
obj1=Demo()
obj2=Demo()

obj3=obj1
del obj1
print("End Code")