import socket
import pandas as pd

#import cs

test=pd.read_csv("data.csv")
#print(test)

s=socket.socket()
print("Socket is created")
s.bind(("192.168.93.105",1801))
s.listen(3)
print("Waiting for Connection")
while True:
	c,addr=s.accept()
	print("Connected with ",addr)
	c.send(bytes("Welcome to server","utf-8"))
	srn=c.recv(1024).decode()	
	df = pd.DataFrame(test, columns = ['SRN', 'NAME'])
	for i in range(len(df)):
  		if srn==str(df.loc[i, "SRN"]):	name=df.loc[i, "NAME"]


	c.send(bytes(name,"utf-8"))
	
	c.close()