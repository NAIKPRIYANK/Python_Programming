def fact(num):
    factori=1
    for i in range(num,0,-1):
        factori*=i

    print("The factorial of {} is {} ".format(num,factori))
num=int(input("Enter the number: "))
fact(num)
