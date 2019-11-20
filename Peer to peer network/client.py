import socket
s=socket.socket()
port=12345
s.connect(('127.0.0.1',port))
print("Connected to server")
while(1):
	inp=s.recv(1024).decode()
	print("Server>> "+str(inp))
	message=input("You>> ")
	s.send(message.encode())