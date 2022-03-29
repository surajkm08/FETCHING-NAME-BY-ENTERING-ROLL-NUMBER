import socket
c=socket.socket()
c.connect(("192.168.93.105",1801))
print(c.recv(1024).decode())
srn=input("Enter the roll no: ")
c.send(bytes(srn,"utf-8"))
print(c.recv(1024).decode())