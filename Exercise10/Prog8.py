num=int(input("Enter the number: "))
for i in range(1,6):
    for j in range(1,6):
        print(chr(num),end=" ")
        num-=1
    num+=j
    print()