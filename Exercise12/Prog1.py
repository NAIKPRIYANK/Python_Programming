rows=int(input("Enter the rows: "))
num=0
temp=3
for i in range(0,rows):
    for j in range(0,rows):
        print(num,end=" ")
        num+=temp
        temp+=2
    print()
