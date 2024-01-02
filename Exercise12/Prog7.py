rows=int(input("Enter the rows: "))
num=69

for i in range(0,rows):
    for j in range(0,rows):
        if(i%2==0):
            print(chr(num),end=" ")
            num-=1
        else:
            print(chr(num),end=" ")
            num+=1
    if(i%2==0):
        num+=1
    else:
        num-=1
    print()