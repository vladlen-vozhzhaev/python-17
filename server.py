import socket
import threading
serverSocket = socket.socket()
serverSocket.bind(('127.0.0.1', 9123))
serverSocket.listen(1)
sockets = []
print('Сервер запущен!')
def chatting(clientSocket):
    while True:
        data = clientSocket.recv(1024)
        print("Сообщение от клиента: "+data.decode())
        for clientSocket1 in sockets:
            clientSocket1.send(data)

while True:
    print("Ожидаем подключения клиента....")
    clientSocket, addr = serverSocket.accept()
    print("Клиент подключился")
    sockets.append(clientSocket)
    thread = threading.Thread(target=chatting, args=(clientSocket,))
    thread.start()