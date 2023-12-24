Mlist = [1, 2, 3, 4, 5]
# print(Mlist,"mylis")

for i in iter(Mlist):
    print(i)



itr = iter(Mlist)
# print(itr,"itr")
try:

    print(next(itr)) 
    print(next(itr)) 
    print(next(itr))  
    print(next(itr))  
    print(next(itr))  
    print(next(itr))  
except StopIteration:
    pass
