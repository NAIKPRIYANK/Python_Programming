char=68
num=4
for i in range(1,5):
    for j in range(1,5):
        print(chr(char),num,end="  ")
        char-=1
        num-=1
    print()
    char+=j
    num+=j
