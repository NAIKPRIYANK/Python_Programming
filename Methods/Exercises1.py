
def fun(lis,sEle):
    count=0;

    for i in lis:
        if(i==sEle):
            count= count+1

    return count
lis=[1,2,3,4,5,4,3,2,4]
searchEl=int(input("Enter the num: "))
cnt=fun(lis, searchEl)
print(cnt)


