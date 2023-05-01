class Point:
    __x = 0
    __y = 0

    def __init__(self, x ,y):
        self.__y = y
        self.__x = x
        print(self)

    def getCoor(self):
        return (self.__x,self.__y)

    def setCoor(self, x ,y):
        self.__y = y
        self.__x = x

    def __del__(self):
        print(self)