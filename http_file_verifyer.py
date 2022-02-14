import http.client

print("---THIS-PROGRAM-FINDS-THE-URL-OF-A-SERVER---\n")

host = input("---INSERT-THE-HOSTS-IP---\n")
port = input("---INSERT-THE-PORT(default:80)---\n")
url = input("---INSERT-THE-URL---\n")

if(port == ""):
	port = 80

try:
    connection = http.client.HTTPConnection(host, port)	
    connection.request('GET', url)
    response = connection.getresponse()
    print('---SERVER-RESPONSE---\n',response.status)
    connection.close()
except ConnectionRefusedError:
      print("\n---CONNECTION-FAILED---")    