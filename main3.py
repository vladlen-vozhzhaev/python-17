# cars = ["bmw", "audi", "kia", "vaz"]
# print(cars[0])
# print(cars[1])
# print(cars[2])
# print(cars[3])
# print( len(cars) )
# i = 0
# while i<len(cars):
#     print(cars[i])
#     i += 1 # i = i + 1


# for car in cars:
#     print(car)

# marks = [4,5,5,5,4,4,5]
# sum = 0
# for mark in marks:
#     sum = sum + mark
#
# print(round(sum / len(marks)))

# Найти максимальный и нечёнтный элемент списка

# import math
#
# numbers = [-420,-234,-253,-23,-326,-56]
# max = -math.inf
# for number in numbers:
#     print(number %  2)
#     if max < number and number %  2 != 0:
#         max = number
#
# print(max)

# Имеется набор букв ["К", "Л", "М", "Н"]
# Необходимо вывести на экран все возможные комбинации 4х символьных слов из этих букв
# Каждая строка должна быть пронумерована
# Найти на какой по счёту строке находится слово "МНКЛ"
# Пример вывода:
# 1) КККК
# 2) КККЛ
# 3) КККМ
# 4) КККН
# 5) ККЛК
# 6) ,,,

# chars = ["К", "Л", "М", "Н"]
# counter = 1
# searchPosition = 0
# for char1 in chars:
#     for char2 in chars:
#         for char3 in chars:
#             for char4 in chars:
#                 word = char1+char2+char3+char4
#                 if word == "МНКЛ":
#                     searchPosition = counter
#                 print(str(counter)+")", word)
#                 counter += 1
# print("Искомая строка МНКЛ находится на позиции: ", searchPosition)

chars = ['К', 'Л', 'М', 'Н']
string1 = "МНКЛ"
i = 0
memory = -1
while i < 256:
    char1 = chars[i % 4]
    char2 = chars[(i // 4) % 4]
    char3 = chars[(i // 16) % 4]
    char4 = chars[(i // 64) % 4]
    string = f"{char4}{char3}{char2}{char1}"
    if string == string1:
        memory = i
    print(f"{i+1}: {string}")
    i += 1
if memory == -1:
    print(f"Строка {string1} не найдена")
else:
    print(f"Строка {string1} имеет индекс {memory+1}")