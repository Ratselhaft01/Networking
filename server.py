import socket
import threading
import random

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

encourage = ["Every second you dwell on the past you steal from your future. Every minute you spend focusing on your problems you take away from finding your solutions.",
"Too often we underestimate the power of a touch, a smile, a kind word, a listening ear, an honest compliment, or the smallest act of caring, all of which have the potential to turn a life around.",
"A bend in the road is not the end of the road…Unless you fail to make the turn.", "The meaning of life is to find your gift. The purpose of life is to give it away.", "Correction does much, but encouragement does more.",
"When everything seems to be going against you, remember that the airplane takes off against the wind, not with it.", "If you ever think about giving up, remember why you held on for so long.", 
"Life is very interesting... in the end, some of your greatest pains, become your greatest strengths.", "Hope sees the invisible, feels the intangible, and achieves the impossible.", 
"If you don't pay appropriate attention to what has your attention, it will take more of your attention than it deserves."]
advice = ["“Think before you speak. Read before you think.”", "“Everything in moderation, including moderation.”", '“The past is behind, learn from it. The future is ahead, prepare for it. The present is here, live it.”', 
'“The past is behind, learn from it. The future is ahead, prepare for it. The present is here, live it.”', '“Never lie in bed at night asking yourself questions you can\'t answer.”', 
'“The most important thing to do if you find yourself in a hole is to stop digging.”', '“Love unconditionally, laugh intentionally, live strategically, and learn daily.”', 
'“Don\'t start a fight just because it\'s the easiest thing to do.”', '“Seek to be the smartest in a room, not the loudest.”', 
'“Find joy in everything you choose to do. Every job, relationship, home… it\'s your responsibility to love it, or change it.”', 
'“Read everything and be kind.”', '“Never miss a good chance to shut up.”', '“We cannot change the cards we are dealt, just how we play the hand.”']
comebacks = ["I’d slap you but I don’t want to make your face look any better.", "Everyone’s entitled to act stupid once in a while, but you really abuse the privilege.", 
"You’re not stupid! You just have bad luck when you’re thinking.", "I may love to shop but I will never buy your bull.", "I may love to shop but I will never buy your bull.",
"Someday you’ll go far. I hope you stay there.", "Were you born this stupid or did you take lessons?", "The people who tolerate you on a daily basis are the real heroes.", "You should really come with a warning label.", 
"I don’t know what your problem is, but I’m guessing it’s hard to pronounce.", "It’s kind of hilarious watching you try to fit your entire vocabulary into one sentence.",
"I’ll never forget the first time we met. But I’ll keep trying.", "I thought of you today. It reminded me to take out the trash.", 
"Stupidity isn't a crime, so you’re free to go.", "You are more disappointing than an unsalted pretzel."]

def send(conn, msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    conn.send(send_length)
    conn.send(message)

def options(conn, choice):
    if choice == "1":
        send(conn, random.choice(encourage))
    
    elif choice == "2":
        send(conn, random.choice(advice))
    
    elif choice == "3":
        send(conn, random.choice(comebacks))
    
    else: send(conn, "That was not an option.")

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            options(conn, msg)
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] server is starting...")
start()

