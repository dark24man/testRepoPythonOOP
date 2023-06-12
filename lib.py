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

class Chess:

    __x = 0
    __y = 0
    __MinCoor = 1
    __MaxCoor = 8

    def __init__(self,x,y,testCoor):
        if testCoor(self,x):
            self.__x = x
        if testCoor(self, y):
            self.__y = y


    @classmethod
    def testCoor(cls,value):
        return Chess.__MinCoor <= value <= Chess.__MaxCoor

    def getCoor(self):
        return (self.__x,self.__y)

    def setCoor(self, x, y):
        self.__y = y
        self.__x = x

    def __getattribute__(self, item):
        if item == "setCoor":
            print('You are using setCoor')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == '_Chess__x' or key == '_Chess__y':
            if not self.testCoor(value):
                raise Exception('no')
        object.__setattr__(self,key,value)


    def __getattr__(self, item):
        print('getattr was called')

    def __delattr__(self, item):
        print('delattr was called')





    @staticmethod
    def gip(x,y):
        return (x**2 + y**2)**0.5


class User:


    __name = ''
    __id = 0
    __balance = 0

    def __init__(self, object=None):
        if object is None:
            self.__id = 0
        else:
            self.__id = object.__id + 1
        self.__name = f'user{self.__id}'

    @property
    def Name(self):
        return  self.__name

    @Name.setter
    def Name(self, name):
        self.__name = name

    @property
    def Balance(self):
        return  self.__balance

    @Balance.setter
    def Balance(self, balance):
        self.__balance = balance

















