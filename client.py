import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "10.50.174.56" 
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    msg_length = client.recv(HEADER).decode(FORMAT)
   
    if msg_length:
        msg_length = int(msg_length)
        msg = client.recv(msg_length).decode(FORMAT)
        print(msg)


def start():
    while True:
        print("_\n\nOptions:\n1) Encouragement\n2) Advice\n3) Comebacks\n4) Quit Program")
        choice = input("\n>>> ")
        if choice == "4":
            send(DISCONNECT_MESSAGE)
            break
        send(choice)

start()