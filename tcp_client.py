import socket

target_host = "google.com"
target_port = 80


#create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET for IPv4 address & SOCK_STREAM for TCP client

# connect to client
client.connect((target_host,target_port))   #giving target host &target port as tuple in argument

#send some data
client.send(b"GET / HTTP/1.1\r\nHost:google.com\r\n\r\n")

#receive some data
response = client.recv(4096)   #size of response as argument
print(response.decode())

client.close()
