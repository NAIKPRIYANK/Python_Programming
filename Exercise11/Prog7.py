num=1
row=int(input("enter the num: "))
for i in range(1,row):
    for j in range(0,i):
        print(num,end=" ")
        num+=1
    num-=1
    print()