num=0
row=int(input("enter the num: "))
for i in range(1,row):
    num=num+i
    temp=num
    for j in range(0,i):
        print(temp,end=" ")
        temp-=1
    print()