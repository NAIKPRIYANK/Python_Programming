def fun(*argv):
    print(argv)
    print(type(argv))
    for i in argv:
        print(i)
    

fun(10,20,30,40,50)
