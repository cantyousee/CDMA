import socket
import pickle
from walshrecur import gen
from cdmasup import twopow

print("enter the number of users: ")
numuser = int(input())
tempnumuser = numuser
tempnum = twopow(numuser)
print(tempnum)

numuser = tempnum
x = [[1]]
perlist = gen(x, tempnum)

for i in range(len(perlist)):
	print(perlist[i])
	
print("enter data for each user")
userdata = [-1 for k in range(numuser)]

for i in range(tempnumuser):
	userdata[i] = int(input())
	if userdata[i] == 0:
		userdata[i] = -1
	elif userdata[i] == 1:
		userdata[i] = 1
	else:
		userdata[i] = 0

print("USERDATA");
print(userdata)
print("\n");

temperlist = [0 for k in range(numuser)]
comchannel = perlist
sum0 = 0
comsum = [0 for k in range(numuser)]

i = 0
j = 0
for i in range(len(perlist)):
	for j in range(len(perlist)):
		comchannel[i][j] = userdata[i] * perlist[i][j]
		comsum[i] = comsum[i] + comchannel[i][j]
		
		
for i in range(len(comchannel)):
	for j in range(len(comchannel)):
		temperlist[j] = temperlist[j] + comchannel[i][j] 
		
print("DATA SENT TO THE SERVER");	
print(temperlist, "\n")
#print(comsum, "\n")
for i in range(numuser):
	print(comchannel[i])
	
	
	
	
soc = socket.socket()
soc.connect(('localhost', 8080))
data=pickle.dumps(temperlist)
soc.sendall(data)
soc.close()	
	
#data=pickle.dumps(y)
#s.send(data)
