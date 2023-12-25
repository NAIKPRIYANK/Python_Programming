print("Hello")
def fun(**argv,x,y):#SyntaxError: invalid syntax
    #Prototype:keyword argument should be single in a function
    print(type(argv))
    print(argv)
fun(x=10,p=20,z=30)


