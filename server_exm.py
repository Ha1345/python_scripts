import socket

SRV_ADDR = input("Type the server's ip address: ")
SRV_PORT = int(input("Type the server's port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)
print("server has started! waiting for connection...")
connection, address = s.accept()
print('client connnected with address: \n', address)
while 1:
	data = connection.recv(1024)
	if not data: break
	#connection.send(b'-- MESSAGE RECEIVED --\n')
	print(data.decode("utf-8"))
connection.close()	
