import socket
import pickle
class abc():
    def __init__(self,type,msg):
        self._type = type
        self._msg= msg
    def get_type(self):
        return self._type
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
clientSocket.connect(("127.0.0.1",9090));
print("client connected")
dataFromServer = clientSocket.recv(1024);
print(dataFromServer.decode());
send_more= True



a = abc('eee','dddd')
while send_more:
    data= input("Enter message to be sent")
    clientSocket.send(pickle.dumps(a));
    dataFromServer = clientSocket.recv(1024); 
    print(dataFromServer.decode());    
    ask = input("Send more messages y/n")
    if ask.lower()=='n':
        break
        
        
