class Demo():
    z=30
    def __init__(self) -> None:
        self._x=10
        self.__y=20
obj=Demo()
# print(obj.__y)#Private Specifier
print(obj._x)#Protected Specifier
print(obj.z)#Public Specifier
