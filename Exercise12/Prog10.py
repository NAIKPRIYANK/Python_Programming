rows=int(input("Enter the rows: "))
num1=2
for i in range(0,rows):
    num=65
    
    for j in range(0,rows):
        if(j%2==0):
            print(chr(num),end=" ")
            num+=2
        else:
            print(num1,end=" ")
            num1+=2
         
    print()