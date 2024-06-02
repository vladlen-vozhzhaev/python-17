import socket
import threading
clientSocket = socket.socket()
clientSocket.connect(('127.0.0.1', 9123))
def sendMessage():
    while True:
        try:
            text = input("Введите сообщение:")
            clientSocket.send(text.encode())
        except:
            break

def getResponse():
    while True:
        response = clientSocket.recv(1024)
        print(response.decode() + "\nВведите сообщение:")

thread = threading.Thread(target=getResponse)
thread.start()
sendMessage()