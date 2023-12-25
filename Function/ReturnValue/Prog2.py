def addByTen(x,y,z):
    x+=10
    y+=10
    z+=10
    return x,y,z

value1=int(input("enter the Value: "))
value2=int(input("enter the Value: "))

value3=int(input("enter the Value: "))
a,b,c=addByTen(value1,value2,value3)

retValue=addByTen(value1,value2,value3)
print(a)
print(b,c)
print(retValue)

print("--------------------------------------------")

print(type(retValue))
for i in retValue:
    print(i)



a,b,c=int(input("ENter the Numbers"))

