"""
loop=True
while(loop==True):


    print("1.DigitCount")
    print("2.EvenDigitCount")
    print("3.OddDigitCount")
    print("4.Exit")
    print("Enter your Choice: ")
    no=123456
    choice=int(input())
    lis=[]
    
    if(choice==1):
        def digitCount(num):
            count=0 
            while(num>0):
                count=count+1
                num=num//10
            lis.append(count)
            print(lis)
            return lis
        print("Total digit count: ",digitCount(no))
    elif(choice==2):
        def EvenDigitCount(num):
            count=0
            while(num>0):
                rem= num%10
                if(rem%2==0):
                    count=count+1
                num=num//10
            lis.append(count)
            return lis
        print("Even Digit count: ",EvenDigitCount(no))
    elif(choice==3):
        def OddDigitCount(num):
            count=0
            while(num>0):
                rem= num%10
                if(rem%2==0):
                    count=count+1
                num=num//10
            lis.append(count)
            return lis
        print("Odd Digit count: ",OddDigitCount(no))
    elif(choice==4):
        loop=False  

"""
def ParFun():
    def digitCount(num):
        count=0
        while(num>0):
            count=count+1
            num=num//10
        lis.append(count)
        return lis
    def oddDigitCount(num):
        count=0
        while(num>0):
            rem= num%10
            if(rem%2==0):
                count=count+1
            num=num//10
        lis.append(count)
        return lis
    def evenDigitCount(num):
        count=0
        while(num>0):
            rem= num%10
            if(rem%2==0):
                count=count+1
            num=num//10
        lis.append(count)
        return lis
    return digitCount,oddDigitCount,evenDigitCount

loop=True
lis=[]
while(loop==True):

    obj1,obj2,obj3=ParFun()

    print("1.DigitCount")
    print("2.EvenDigitCount")
    print("3.OddDigitCount")
    print("4.Exit")
    print("Enter your Choice: ")
    no=123456
    choice=int(input())
    
    if(choice==1):
        print(obj1(no))

    elif(choice==2):
        print(obj3(no))

    elif(choice==3):
        print(obj2(no))
    elif(choice==4):
        loop=False
        print("'-'Thank You'-'")

