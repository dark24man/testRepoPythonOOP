# from lib import Point
# from lib import Chess
#
# a = Chess(5,5)
# a.setCoor(40,30)
# print(a.getCoor())
# c = Chess(0,9)
#
#
# a = Chess(10,20)
# b = Chess(100,200)
# print(b.getCoor())

from  lib import  User


users = [User()]
for i in range(10):
    users.append(User(users[i]))

for i in range(len(users)):
    print(users[i].__dict__)

