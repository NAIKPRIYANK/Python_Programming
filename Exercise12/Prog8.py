rows=int(input("Enter the rows: "))
num=1

for i in range(0,rows):
    for j in range(0,rows):
        if(i%2==0):
            print(num,end=" ")
            
        else:
            print(num**2,end=" ")
        num+=1
    print()