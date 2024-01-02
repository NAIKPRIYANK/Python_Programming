rows=int(input("Enter the rows: "))


for i in range(0,rows):
    num=68
    num1=1
    for j in range(0,rows):
        print(num1,chr(num),end="  ")
        num-=1
        num1+=1
    print()