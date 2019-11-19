import socket
import datetime
from timeit import default_timer as timer
from dateutil import parser 
s=socket.socket()
port=12345
s.connect(('127.0.0.1',port))
request=timer()
servert=parser.parse((s.recv(1024)).decode())
response=timer()
rtt=response-request
synctime=servert+datetime.timedelta(seconds = (rtt) / 2) 
print(synctime)
s.close()