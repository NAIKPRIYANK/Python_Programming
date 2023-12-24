num=92738923
count=0
while(num>0):
    rem=num%10
    if(rem%2==1):
        count+=1
    num=num//10
print(count)