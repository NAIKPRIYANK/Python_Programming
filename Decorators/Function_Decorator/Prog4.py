def decorFun(fun):
    def wrapper():
        print("Start Wrapper")
        fun()
        print("End Wrapper")
    return wrapper
@decorFun
def normalfun():
    print("In Normal fun")

#normalfun=decorFun(normalfun)
normalfun()
