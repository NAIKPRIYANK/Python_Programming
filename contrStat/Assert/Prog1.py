name=input("enter Your name:")
age=int (input("ENter your age: "))
assert age>0,"Age must be Positive"
if age>18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")
