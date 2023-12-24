num=372
temp=num
length=len(str(num))
add=0
while(num>0):
    rem=num%10
    add=add+rem**length
    num=num//10
if(temp==add):
    print(temp," is a armstrong number")

    