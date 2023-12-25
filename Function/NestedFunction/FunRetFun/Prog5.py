def outer ():
    def inner1(x,y):
        print("inner1")
    return inner1
    print("Inner2")


retObj=outer()
retObj(10,20)
