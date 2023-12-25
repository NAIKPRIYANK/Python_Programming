print("function")
def Outer():
    def inner1():
        print("In Inner Function")

    def inner2():
        print("In Inner Function")

    print("In Outer Funtion")
Outer().inner1()#AttributeError: 'NoneType' object has no attribute 'inner1'

