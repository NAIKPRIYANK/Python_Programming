num=496
i=1
add=0
while(i<=num//2):
    if(num%i==0):
        add=add+i
    i+=1

print(add)
if(add==num):
    print(num ," is a perfect number")

