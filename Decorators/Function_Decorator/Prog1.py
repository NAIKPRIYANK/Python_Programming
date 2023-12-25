def funOuter():
    print("In Outer function")

    def innerFun1():
        print("Inner fun-1")

    def innerFun2():
        print("Inner fun-2")
    return innerFun1,innerFun2
#Type-1
'''
    innerFun1()
    innerFun2()
funOuter()
'''

#Type-2
'''
obj1,obj2=funOuter()
obj1()
obj2()
    
'''

#Type-3
'''
obj=funOuter()
for x in obj:
    x()
    '''

#Type-4

obj=funOuter()
obj[0]()
obj[1]()
