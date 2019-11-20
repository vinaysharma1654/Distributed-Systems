import socket
s=socket.socket()
port=12345
s.bind(('',port))
s.listen(5)
c,addr=s.accept()
print("connected to "+str(addr))
while(1):
	message=input("You>> ")
	c.send(message.encode())
	# c.listen(5)
	a=c.recv(1024).decode()
	print("Client>> "+str(a))