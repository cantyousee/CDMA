import socket
import pickle
from walshrecur import gen

c = 'N'
while c == 'N':
	socob = socket.socket()
	socob.bind(('0.0.0.0', 8080))
	socob.listen(5)
	con, addr = socob.accept()
	print("Got connection from", addr)
	data = pickle.loads(con.recv(1024))
	print(data)
	con.close()

	templist = data
	numuser = len(data)
	print("MAX NUMBER OF USERS: ", numuser)
	x = [[1]]
	perlist = gen(x, numuser)
	sum = [0 for k in range(numuser)]
	for i in range(numuser):
		for j in range(numuser):
			sum[i] = sum[i] + perlist[i][j] * data[j]
		sum[i] = sum[i] / numuser

	print(sum)
	
	c = input("Shut the server?  Y/N: ")

		 
