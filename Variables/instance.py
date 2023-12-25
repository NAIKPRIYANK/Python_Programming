#Ex1
'''
class Employee:
    def __init__(self,empID,empName):

        print("In constructor")
        self.empID=empID
        self.empName=empName

    def empInfo(self):
        print(self.empID)
        print(self.empName)

emp1=Employee(1,"Kanha")
emp2=Employee(2,"Ashish")

emp1.empInfo()
emp2.empInfo()'''

#Ex2

#instnce and class variable
class Company:
    compName="Facebook"

    def __init__(self):
        print("In constructor")
        self.empId=12
        self.empName="Priy"

    def compInfo(self):
        print(self.empId)
        print(self.empName)
        print(compName)
emp1=Company()
emp1.compInfo()
