def fun():
    print("Start fun")
    yield 10
    yield 20
    yield 30
    print("End Fun")

ret=fun()
for i in ret:
    print(i)