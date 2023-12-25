def gun():
    print("In gun")
def fun(x):
    print("In fun")
    return x

def run(y):
    print("In run")
    y()

run(fun(gun))
