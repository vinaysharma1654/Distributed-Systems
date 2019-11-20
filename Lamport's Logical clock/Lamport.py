import multiprocessing
def sender(conn,t):
	t+=1
	conn.send(t)
	return(t)
def receiver(conn):
	t=conn.recv()
	return(int(t)+1)

def process1(conn):
	t=0
	t=sender(conn,t)
	t+=1 #Event
	t=max(receiver(conn),t+1)
	print("process1 timer=",t)
def process2(conn):
	t=0
	t+=2
	t=max(receiver(conn),t+1)
	t=sender(conn,t)
	print("process2 timer=",t)
if __name__ == '__main__':
	a,b=multiprocessing.Pipe()
	p1=multiprocessing.Process(target=process1,args=(a,))
	p2=multiprocessing.Process(target=process2,args=(b,))

	p1.start()
	p2.start()

	p1.join()
	p2.join()