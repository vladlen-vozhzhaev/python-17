# Макс. уровень здоровья (hp) может быть не более 100
class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.__hp = 100
    def sayHi(self, name):
        print(f"Привет {name}, меня зовут {self.name}")

    def get_private_hp(self):
        return self.__hp
    def set_private_hp(self, value):
        if self.__hp+value >= 100:
            self.__hp = 100
        else:
            self.__hp += value

person1 = Person("Иван", "Иванов", 23)
person2 = Person("Вася", "Пупкин", 34)
person3 = Person("Алекс", "Петров", 39)
medKit = 500000
print(person1.get_private_hp())
person1.set_private_hp(-30)
print(person1.get_private_hp())
person1.set_private_hp(medKit)
print(person1.get_private_hp())
# print(person1.name)
# print(person2.lastname)
# print(person1.age)
# person1.sayHi(person2.name)
# person2.sayHi(person3.name)
# person3.sayHi(person1.name)
