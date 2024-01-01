class Demo():
    z=30
    def __init__(self) -> None:
        self._x=10
        self.__y=20
print(dir(Demo))
obj=Demo()
# print(obj.__y)#Private Specifier-----Error
print(obj._x)#Protected Specifier
print(obj.z)#Public Specifier
print(obj._Demo__y)#Private Specifier
print(dir(obj))


