class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age
    def sayHi(self, name):
        print(f"Привет {name}, меня зовут {self.name}")

person1 = Person("Иван", "Иванов", 23)
person2 = Person("Вася", "Пупкин", 34)
person3 = Person("Алекс", "Петров", 39)

# print(person1.name)
# print(person2.lastname)
# print(person1.age)
person1.sayHi(person2.name)
person2.sayHi(person3.name)
person3.sayHi(person1.name)