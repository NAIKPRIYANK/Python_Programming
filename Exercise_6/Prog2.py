num=6
i=2
count=0
while(i<=num//2):
    if(num%i==0):
        count+=1
    i+=1
print(count)
if(count>0):
    print(num," is not a prime number")