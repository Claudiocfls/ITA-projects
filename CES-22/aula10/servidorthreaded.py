
# esse é o servidor do chat multiusuário
# ele deve ser executado antes dos clientes em clientesimples.py


import socket
import threading
from time import ctime

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.client_list = []

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            if client:
                self.client_list.append(client)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    # Set the response to echo back the recieved data
                    dict_received = eval((data).decode('utf-8'))
                    print("%s diz: %s" % (dict_received['nome'], dict_received['data']))
                    for c in self.client_list:
                        if c != client:
                            c.send(('\n'+ctime()+': \n' + dict_received['nome'] + ' diz: '+dict_received['data']).encode('utf-8'))
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                print("Exception")
                return False
if __name__ == "__main__":
    while True:
        port_num = 21567 #input("Port? ")
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

    ThreadedServer('',port_num).listen()
