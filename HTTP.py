import http.client

print("** This program returns a list of methods if OPTIONS is enabled **\n")

host = input("---INSERT-THE-HOSTS-IP---\n")
port = input("---INSERT-THE-PORT(default:80)---\n")

if(port == ""):
	port = 80

try:
    connection = http.client.HTTPConnection(host, port)	
    connection.request('OPTIONS', '/')
    response = connection.getresponse()
    print("---ENABLED-METHODS-ARE---\n",response.getheader('allow'))
    connection.close()
except ConnectionRefusedError:
      print("\n---CONNECTION-FAILED---")    