# Creator :- AnonyMSAV Contact :- https://www.t.me/Anony4790
import socket
import threading
import time

HEADER = 256
PORT = 5555
IP_Address = socket.gethostbyname(socket.gethostname())
Address = IP_Address,PORT

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(Address)

def send(msg):
    content =  msg.encode('utf-8') # Encode msg to utf-8 format.
    content_len = len(content) # Messure msg length.
    send_length = str(content_len).encode('utf-8')
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(content)
    print(client.recv(2048).decode('utf-8'))

def main():
    receive = client.recv(2048).decode('utf-8') # Receive  'Name' messeage from server socket.
    if('Name' in receive):
        user =  input('Enter Name : ')
        client.send(user.encode('utf-8'))
    
    while True:
        msg = input('Enter : ')
        send(msg)
        if(msg == '#Leave'):
            print('Stoping ...')
            time.sleep(2)
            return False

main()



