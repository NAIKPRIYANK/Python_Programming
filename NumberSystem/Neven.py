num=1
for i in range(5):
    
    for j in range(5):
        
        while(num<=60):
            Sum=-1
            n=num
            digit=0
            count=0
             while(n>0):
                 digit=n%10
                 Sum= Sum+digit
                 n=n//10


             if(num%Sum==0):
                 print(num,end=" ")
                 count=+1
            if count>5:
                break
            num+=1

    print()
