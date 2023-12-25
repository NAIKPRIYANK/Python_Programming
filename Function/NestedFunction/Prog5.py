def outer():
    def inner():
        print("in Inner Function")

    inner()
    print("In outer function")
print("Starr code")
outer()
print("End Code")


