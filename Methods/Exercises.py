#Exercise1
'''
def outer():
    def inner():
        return"hello, I'm the inner function"
    return inner()
ans=outer()
print(ans)




#Exercise2
def outer():
    def inner():
        return "hello, I am inner function"
    return inner
retObj=outer()
retInner=retObj()
print(retInner)


#Exercise3
import array as arr

def fun(ar):
    a=0
    for i in ar:
        fact=1;
        for j in range(1,i+1):
            fact=fact*j;
        ar[a]=fact
        a=a+1
    return ar

numArray=arr.array('i',[2,3,4,5,6,7])
arrafact=fun(numArray)
print(arrafact)



#Exercise4

def fun(lis,sEle):
    count=0;

    for i in ls:
        if(i==sEle):
            count= count+1

    return count
lis=[1,2,3,4,5,4,3,2,4]
searchEl=int(input("Enter the num: "))
fun(lis, searchEl)



