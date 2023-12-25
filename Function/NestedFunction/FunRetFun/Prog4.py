def outer():
    def inner1(x,y):
        print("In inner1")
        return x+y
    def inner2(a,b):
        print("In inner2")
        return a*b

    return inner1,inner2
inn1,inn2= outer()
ret1=inn1(20,30)
ret2=inn2(10,20)
print(ret1+ret2)
print(inn1)
print(inn2)



