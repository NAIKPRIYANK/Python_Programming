def fact(num):
    res=1
    for i in range(1,num+1):
        res=res*i
    return res
num=146
temp=num
add=0
while(num>0):
    rem=num%10
    add=add+fact(rem)
    num=num//10
if(temp==add):
    print(temp," is a strong number")