rows=int(input("Enter thr num: "))
num=69

for i in range(rows,0,-1):
    temp=num
    for j in range(0,i):
        print(chr(temp),end=" ")
        temp+=1
    num-=1
    print()