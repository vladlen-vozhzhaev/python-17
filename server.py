import socket # Подключаем сокет (сокет - ip + port)
import threading # Подключает (поток исполнения, нужен для многопоточности)
serverSocket = socket.socket() # Создаём серверный сокет
serverSocket.bind(('45.80.70.14', 9123)) # Открываем порт
serverSocket.listen(1) # Разрешаем запускаться одному экземпляру программы для прослушки порта
sockets = [] # Переменная для хранения списка сокетов
print('Сервер запущен!')
def chatting(clientSocket): # ф-ция для приёма и рассылки сообщений
    try: # Пытаться получить от клиента сообщение
        clientSocket.send("Сервер: Введите имя ".encode())
        data = clientSocket.recv(1024)
        name = data.decode()
        while True:
            data = clientSocket.recv(1024)
            req = name+": "+data.decode()
            print(req)
            for clientSocket1 in sockets:
                clientSocket1.send(req.encode())
    except: # Если связь с клиентом потеряна
        print("Пользователь покинул чат")
    finally: # Это блок работает и в случае успешного выполнения try и в случае ошибки
        sockets.remove(clientSocket) # Удаляем отключившегося клиента из списка
        clientSocket.close() # Закрывает соединение с клиентом

while True: # Бесконечный цикл
    print("Ожидаем подключения клиента....")
    clientSocket, addr = serverSocket.accept() # Ожидаем подключения клиента....
    print("Клиент подключился")
    sockets.append(clientSocket) # Добавляем подключившегося в список
    thread = threading.Thread(target=chatting, args=(clientSocket,)) # Создаём поток, для запуска ф-ции приёма и передачи сообщений
    thread.start() # Запускаем поток