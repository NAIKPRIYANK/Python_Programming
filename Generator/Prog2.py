def fun():
    print("Start Fun")
    yield 10
    yield 20
    yield 30
    print("End Fun")
    yield 
#type-1
# ret,set,tet=fun()
ret=fun()

# print(fun())
# print(ret)
# print(set)
# print(tet)

print(next(ret)) 
print(next(ret)) 
print(next(ret))
print(next(ret))  
    











#type-2
# ret=fun()
# try:

#     print(next(ret))
#     print(next(ret))
#     print(next(ret))
#     print(next(ret))

# except StopIteration:
#     pass

