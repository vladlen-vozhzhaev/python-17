# name = input("Введите имя: ")
# print("Hello "+name+"!")
# a = float(input("Введите число: "))
# b = float(input("Введите число: "))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a**b)
# print(a%b) # 15%6 = 3
# print(a==b)
# print(a>b)
# Кассир вводит стоимость товара и кол-во
# Кассир вводит сумму которую дал покупатель
# Программа должна показать сумму сдачи
price = int(input("Введите стоимость товара: "))
quantity = int(input("Введите кол-во ед. товара: "))
result = price*quantity
print("Итого: "+str(result))
summ = int(input("С какой суммы необходимо выдать сдачу: "))
print(summ - result)
