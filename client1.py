import socket
import threading

def connectionen():

    global server, username, message_handler, input_elleyici
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            HOST = input("host ip: ")
            PORT = int(input("host port: "))
            server.connect((HOST, PORT))
            break
        except:
            print("hay aksi ehehe")
        
    username = input("bir rumuz girin: ")
    server.send(username.encode())

    message_handler = threading.Thread(target=handle_messages, args=())
    message_handler.start()

    input_elleyici = threading.Thread(target=input_elleyici, args=())
    input_elleyici.start()

def handle_messages():
    while True:
        print(server.recv(1024).decode())

def input_elleyici():
    while True:
        server.send((username + ': ' + input()).encode())

connectionen()