import socket
import os
SRV_ADDR = input("Type the server's ip address: ")
SRV_PORT = int(input("Type the server's port: "))
user = os.environ.get("USER")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SRV_ADDR, SRV_PORT))
print("server is connected")
message = input("type your message:")
s.send(user.encode())
s.send("\n".encode())
s.send(message.encode())
s.close()