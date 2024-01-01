num=1
rows=int(input("Enter the number: "))
for i in range(rows,1,-1):
    for j in range(1,i):
        print(num,end=" ")
    num+=1
    print()