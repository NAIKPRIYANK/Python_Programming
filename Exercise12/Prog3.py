rows=int(input("Enter the rows: "))
for i in range(0,rows):
    num1=1
    num2=2
    for j in range(0,rows):
        if(i%2==0):
            print(num2,end=" ")
            num2+=2
        else:
            print(num1,end=" ")
            num1+=2
    print()
