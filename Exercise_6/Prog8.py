num=92729
temp=num
count=0
res=0
while(num>0):
    res=res*10+num%10
    num//=10   
if(res==temp):
    print(temp," is a palindrome")