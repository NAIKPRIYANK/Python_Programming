def outer(x,y):
    def inner():
        print("In Inner")
    print("In outer Function")
    return inner
retObj=outer(10,20)
retObj()
