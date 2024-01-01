class Demo():
    def __init__(self) -> None:
        print("In Constructor")
    def __del__(self):
        print("In Destructor")

#type-1
# def Fun():
#     print("In fun")
#     obj=Demo()
#     print("End Fun")
# Fun()
# print("ENd COde")
        
def Fun():
    print("In Fun")
    obj=Demo()
    print("end fun")
    return obj
retObj=Fun()
print("End COde")