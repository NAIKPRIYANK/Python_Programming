print("Function")
def outer():
    def inner1():
        print("In Inner1 Function")
    def inner2():
        print("In Inner2 Function")
    print("In outer Function")
outer().inner()

