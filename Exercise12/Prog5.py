rows=int(input("Enter the rows: "))
num=1
# temp=2
for i in range(0,rows):
    for j in range(0,rows):
        print(num,end=" ")
        num+=num
    
    print()