

# esse é o cliente do chat multiusuário
# deve ser executado depois do servidor servidorthreaded.py

from socket import *
import threading


HOST = '127.0.0.1' # or 'localhost'
PORT = 21567
BUFSIZ = 1024

tcpCliSock = socket(AF_INET, SOCK_STREAM)
ADDR = (HOST, PORT)
tcpCliSock.connect(ADDR)
host=tcpCliSock.getsockname() #  print client host name
print(host)

nome = (input('Qual o seu nome? '))

data = ''
def read_input():
    while True:
        data = ''
        data = (input('> '))
        if data:
            data_to_send = (str({"nome": nome, "data": data})).encode('utf-8')
            tcpCliSock.send(data_to_send)

def read_server():
    while True:
        data_server = tcpCliSock.recv(BUFSIZ)
        if data_server:
            print(data_server.decode('utf-8'))


threading.Thread(target = read_input).start()
threading.Thread(target = read_server).start()
    
    
# tcpCliSock.close()
