def DecorFun(func):
    print("In Outer Function")
    def Inner(*argv):
        print("Start Inner")
        print(argv)
        val= func(*argv)
        print("End Inner")
        return val
    return Inner
@DecorFun
def normalFun(x,y):
    print("In Normal Function")
    return x+y

print(normalFun(10,20))
