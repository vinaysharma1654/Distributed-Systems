import socket
import datetime as dt
s=socket.socket()
print("socket created successfully")
port=12345
s.bind(('',port))
s.listen(5)
print("socket is listening....")
while True:
	c,addr=s.accept()
	print("connected to "+str(addr))
	c.send(str(dt.datetime.now()).encode())
	c.close()
	break