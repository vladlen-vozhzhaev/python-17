class Hotel:
    def __init__(self, rooms):
        self.rooms = rooms
    def getFreeRooms(self):
        for room in self.rooms:
            if not room.reserved:
                print(room.number)
    def getReservedRooms(self):
        for room in self.rooms:
            if room.reserved:
                print(room.number)
    def reservedRoom(self):
        roomNumber = int(input("Введите номер комнаты: ")) # 33
        error = True
        for room in self.rooms:
            if room.number == roomNumber and not room.reserved:
                print("Комната успешно забронирована")
                room.reserved = True
                error = False
        if error:
            print("Ошибка при бронировании")
    def filter(self):
        place = int(input("Кол-во спальных мест: "))
        tv = input("Наличие tv (Да/Нет/Неважно)")
        wifi = input("Наличие wifi (Да/Нет/Неважно)")
        for room in self.rooms:
            if (
                    room.place == place and
                    (tv == "Да" and room.tv or not room.tv and tv == "Нет" or tv == "Неважно") and
                    (wifi == "Да" and room.wifi or not room.wifi and wifi == "Нет" or wifi == "Неважно")
            ):
                print(room.number)

class Room:
    def __init__(self, number, place, wifi, tv):
        self.number = number
        self.place = place
        self.wifi = wifi
        self.tv = tv
        self.reserved = False

hotel = Hotel([
    Room(11, 2, True, True),
    Room(12, 1, True, False),
    Room(13, 2, True, True),
    Room(21, 4, False, False),
    Room(22, 3, False, True),
    Room(23, 3, True, False),
    Room(31, 1, False, True),
    Room(32, 2, False, True),
    Room(33, 1, True, False),
])
command = input("Введите команду: ")
while command != "exit":
    if command == "getFreeRooms":
        hotel.getFreeRooms()
    elif command == "reserve":
        hotel.reservedRoom()
    elif command == "getReservedRooms":
        hotel.getReservedRooms()
    elif command == "filter":
        hotel.filter()
    command = input("Введите команду: ")