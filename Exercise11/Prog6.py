rows=int(input("Enter the number: "))

for i in range(rows,1,-1):
    num=1
    for j in range(1,i):
        print(num,end=" ")
        if(num==0):
            num=1
        else:
            num=0
    print()