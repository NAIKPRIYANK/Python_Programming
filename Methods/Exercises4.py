class Sum:
    def mySum(self,a,b):
        sum= a+b
        return sum



num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))

s1=Sum()
s2=Sum()
ans1=s1.mySum(num1,num2)
ans2=s2.mySum(num1,num2)
print(id(ans1))
print(id(ans2))


