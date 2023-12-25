def Outer():
    def inner1():
        print("In Inner1 fun")
    def inner2():
        print("In Inner2 Fun")

    print("In Outer Fun")
    inner1()
    inner2()
Outer()


