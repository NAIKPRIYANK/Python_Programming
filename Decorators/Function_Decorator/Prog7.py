def Outer(fun):

    def inner(*argv):

        add=1
        fun(*argv)
        for i in argv:
            add=add*i
:        return add
    return inner

