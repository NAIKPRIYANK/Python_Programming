rows=int(input("Enter the rows: "))
num=1
temp=2
for i in range(0,rows):
    for j in range(0,rows):
        if(i%2==0):
            if(j%2==0):
                print("$",end=" ")
            else:
                print("=",end=" ")
        else:
            if(j%2==0):
                print("=",end=" ")
            else:
                print("$",end=" ")
    print()
            
        