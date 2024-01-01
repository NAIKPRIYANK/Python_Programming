char=int(input("Enter the number: "))
for i in range(1,4):
    for j in range(1,4):
        print(chr(char), end=" ")
        char+=1
    print()
    
