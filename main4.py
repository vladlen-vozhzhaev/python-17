# def f(x):
#     return x**2
#
# print( f(2) )
# print( f(-3) )
# print( f(-4) )
# print( f(5) )

# def login(login, password):
#     if login == "admin" and password == "123":
#         print("Доступ разрешен - ADMIN")
#         return True
#     else:
#         print("Доступ запрещен")
#         return False
#
# while not login( input("Введите логин: "), input("Введите пароль: ") ):
#     pass

# def sayHi(name):
#     print(f"Hello {name}")
#
# sayHi("Ivan")
# sayHi("Alex")
# sayHi("Vasya")

# name = "Ivan"
#
# def changeName():
#     name = "Alex"
#
# changeName()
# print(name)

# Имеется кофемашина, после приготовления кофе, аппарат выдаёт сдачу монетами номиналом рублей РФ
# 1 2 5 10
# Реализовать функцию, которая принимает на вход число (сдача), и выводи на экран сдачу монетами
# 36 = 10 10 10 5 1
# 23 = 10 10 2 1

# def getChange(num):
#     coin = 0
#     if num >= 10: coin = 10
#     elif num >= 5: coin = 5
#     elif num >= 2: coin = 2
#     elif num >= 1: coin = 1
#
#     if coin > 0:
#         print(coin)
#         getChange(num - coin)
#
# getChange(36)

# def f(n):
#     if n>2:
#         return g(n-1)+f(n-2)
#     else:
#         return n
#
# def g(n):
#     if n>2:
#         return f(n-2)+g(n//2)
#     else:
#         return 1
#
# print(g(9))

# g(9) = f(7)+g(4) = 11 + 3 = 14
# f(7) = g(6)+f(5) = 6 + 5 = 11
# g(6) = f(4)+g(3) = 4 + 2 = 6
# f(4) = g(3)+f(2) = 2+2 = 4
# g(3) = f(1)+g(1) = 1+1 = 2
# f(5) = g(4)+f(3) = 3+2=5
# g(4) = f(2)+g(2) = 2+1=3
# f(3) = g(2)+f(1) = 1+1=2

# def f():
#     print("Hello")
#     f()
#
# f()