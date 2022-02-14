import socket

target = input("ENTER THE IP ADDRESS TO SCAN:")
portrange = input("ENTER THE PORT RANGE TO SCAN:")

lowport = int(portrange.split("-")[0])
highport = int(portrange.split("-")[1])

print("scanning host... \n", target,"\n" , "from port... \n", lowport, "to port.. \n", highport)


for port in range(lowport,highport):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	status = s.connect_ex((target,port))
	if status == 0:
		print("####PORT",port,"OPEN####")
	else:
	    print("PORT",port,"~ Closed")
	s.close()