char=int(input("Enter the ascii: "))
for i in range(1,5):
    for j in range (1,5):
        print(chr(char),end=" ")
        char+=1
    char-=j
    print()