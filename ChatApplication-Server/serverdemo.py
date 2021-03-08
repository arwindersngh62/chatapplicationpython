import socket
from _thread import *
import pickle
class abc():
    def __init__(self,type,msg):
        self._type = type
        self._msg= msg
    def get_type(self):
        return self._type
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
	serverSocket.bind(("localhost",9090))
except:
	print(str(e))

print("waiting for connection")
serverSocket.listen(5)
thread_count= 0
def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server\n'))
    while True:
        data = connection.recv(4096)
        reply = 'Server Says: Hello'
        dataclass = pickle.loads(data)
        print(dataclass._type)
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()

while (True):
	Client, address = serverSocket.accept()
	print("connected to server: "+ str(address[0]+":"+str(address[1])))
	id = start_new_thread(threaded_client,(Client,))
	thread_count+=1
	print('Thread Number: ' + str(thread_count))
ServerSocket.close()
	
