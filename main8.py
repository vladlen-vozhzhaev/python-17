class Animal:
    def __init__(self, nickname, age, breed):
        self.nickname = nickname
        self.age = age
        self.breed = breed
    def run(self):
        print(f"{self.nickname} побежал(а)")
    def speak(self):
        print("Звук не назначен")


class Cat(Animal):
    def __init__(self, nickname, age, breed):
        super().__init__(nickname, age, breed)
    def speak(self):
        print("Мяу")


class Bird(Animal):
    def __init__(self, nickname, age, breed):
        super().__init__(nickname, age, breed)
    def fly(self):
        print(f"{self.nickname} полетел(а)")
    def speak(self):
        print("Чик чирык")

class Horse(Animal):
    def __init__(self, nickname, age, breed):
        super().__init__(nickname, age, breed)

horse1 = Horse("Мустанг", 4, "Рысак")
horse1.speak()
# cat1 = Cat("Барсик", 4, "Британец")
# cat2 = Cat("Мурка", 3, "Дворняга")
# bird1 = Bird("Кеша", 7, "Волнистый")
# cat1.run()
# cat2.run()
# bird1.run()
# bird1.fly()
# cat1.speak()
# cat2.speak()
# bird1.speak()