'''for x in range(1,15,3):
    print(x)'''



'''
x = int(input("enter the Number:"))
y = int(input("enter the stop:"))
for i in range(x,y+1):
    print(i)'''




'''for i in range(10,3,-2):
    print(i)'''


'''
for i in range (1, 5):
    sum= 4
    print(sum)
    print(i)
print(sum)
print(i)'''


'''
x = int(input("enter the Number:"))
y = int(input("enter the stop:"))
for i in range(x,y+1):
    if i %2==0:
        print("{} is a even number".format(i))
    else:
        print("{} is odd number".format(i))'''




x = int(input("enter the Number:"))
y = int(input("enter the stop:"))
for i in range(x,y+1):
    if i %3==0 and i%5==0:
        print("{} is a divisible 3 and 5 ".format(i))
