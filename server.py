# Creator :- AnonyMSAV Contact :- https://www.t.me/Anony4790
import socket
import threading


HEADER = 256
PORT = 5555
sort = []
users = []
IP_Address = socket.gethostbyname(socket.gethostname()) 
Address = (IP_Address,PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(Address) # Bind IP address and Port to this socket.


def clients(conn,addr): # Connect server and clients individually.
    print(f'{addr} connected')
    sort.append(conn) # Add client sockets to sort list.
    conn.send('Name'.encode('utf-8')) # Send 'Name' message to clients.
    name = conn.recv(HEADER).decode('utf-8')
    users.append(name) # Add clients name to user list.

    while True: # Wait for recieving connected sockets data.
        length = conn.recv(HEADER).decode('utf-8') # Decode recieved msg with uft-8 format.
        
        if length:
            length = int(length) # Convert msg to integer. It used to get how many bits recive from recieved msg.
            msg = conn.recv(length).decode('utf-8') # Again convert msg to utf-8 format and assign to msg. 

            if(msg == '#Leave'):
                print(f'{addr} left')
                break    # If client socket msg is #Leave it means client want to leave, then loop is breaked.

            print(f'{addr} : {msg}') # To print what client and what it's msg.

            send_msg(msg,conn,name)

    conn.close() # Close client socket connection.

def send_msg(msg,conn,name): # Send messages to other clients.
    for i in sort:
        if(i != server and i != conn): # Send messages except message sender.
            i.sendall(f'{name} > {msg}'.encode('utf-8'))

def start():
    print(f'Server is listening at {IP_Address}')
    server.listen() # Listen new connections.
    
    while True:
        conn,addr = server.accept() # Accept new connection and store its address,port and send infos back that connection.
        thread = threading.Thread(target = clients, args = (conn,addr)) # When new connection occur pass infos to clients()
        thread.start()
        print(f'Connected : {threading.activeCount() -1 }') # To view how many clients are connected. One threads equal one connection.

print('Server is starting...')
start()

