def fact(a):
    factori=1
    for i in range(a,0,-1):
        factori*=i
    return factori
num= int(input("enter the num : "))
factorii= fact(num)
print(factorii)
