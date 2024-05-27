import socket
import threading
clientSocket = socket.socket()
clientSocket.connect(('127.0.0.1', 9123))
def sendMessage():
    while True:
        text = input("Введите сообщение:")
        clientSocket.send(text.encode())
thread = threading.Thread(target=sendMessage)
thread.start()
while True:
    response = clientSocket.recv(1024)
    print("\nСервер: "+response.decode()+"\nВведите сообщение:")