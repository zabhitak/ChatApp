import socket
CHUNK = 65535 #receive at most these bytes of data at once
port = 8000

s  = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # CREATE A SOCKET OBJECT
# socket.socket(family,type)
# AF_NET : family of ipv4 ip address
#SOCK_DGRAM: udp, SOCK_STREAM: TCP 

hostname = '127.0.0.1'

s.bind((hostname,port))

print(f"server is live on {s.getsockname()}")

while True:
    data, clientAdd = s.recvfrom(CHUNK)
    message = data.decode('ascii') # data by default travel in bytes
    print(f"Sarthak : {message}")
    message_send = input("Reply:")
    data = message_send.encode('ascii')
    # send data to the ip add send me the data
    s.sendto(data,clientAdd)