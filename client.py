import socket
CHUNK = 65535
port = 8000

s  = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # CREATE A SOCKET OBJECT\

# instead of explicitly binding the socket, i will let os do it

hostname = '127.0.0.1'

while True:
    s.connect((hostname,port))
    message = input("Type Message:")
    data = message.encode('ascii')
    s.send(data)

    # data received
    data = s.recv(CHUNK)
    text = data.decode('ascii')
    print(f'Abhinav: {text}')