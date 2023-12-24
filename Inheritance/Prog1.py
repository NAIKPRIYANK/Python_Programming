class Company():
    x=10
    def __init__(self,cName,Loc):
        
        print("in Constructor")
        self.cName=cName
        self.Loc=Loc

    def compInfo(self):
        print(self.cName)
        print(self.Loc)

class Employee(Company):
    pass

    

    

# obj1=Company("Beincaps","Pune")
# obj2=Company("Incubator","Pune")

obj1=Employee("Beincaps","Pune")
obj2=Employee("Incubator","Pune")

obj1.compInfo()
obj2.compInfo()

