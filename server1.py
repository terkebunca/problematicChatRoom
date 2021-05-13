import socket 
import threading


HOST = socket.gethostbyname(socket.gethostname())
PORT = 8080
ADDR = (HOST, PORT)

clients = []
username_lookup = {}

def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server.bind(ADDR)
    server.listen(100)

    print('Running on host: '+str(HOST))
    print('Running on port: '+str(PORT))

    while True:
        conn, addr = server.accept()
        username = conn.recv(1024).decode()
        
        print('oğlum çay ver! username: '+ str(username))
        broadcast('oğlum çay ver! username: '+ str(username))

        username_lookup[conn] = username

        clients.append(conn)

        threading.Thread(target=handle_client, args=(conn, addr)).start()

def broadcast(msg):
    for connection in clients:
        connection.send(msg.encode())

def handle_client(conn, addr):
    while True:
        try:
            msg = conn.recv(1024)
        except:
            conn.shutdown(socket.SHUT_RDWR)
            clients.remove(conn)
            print(str(username_lookup[conn] + " mekanı terk etti(maalesef)"))
            broadcast(str(username_lookup[conn] + " mekanı terk etti(maalesef)"))
            break
        if msg.decode != "":
            print("[NEW MESSAGE] " +str(msg.decode()))
            for connection in clients:
                if connection != conn:
                    connection.send(msg)

start()