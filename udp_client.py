import socket

target_host = '127.0.0.1'
target_port = 8000

#socket type to SOCK_DGRAM for UDP connection
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#UDP is connectionless protocol, so no call to connect()
client.sendto(b'ABCDEFGH',(target_host,target_port))

#call recvfrom to get UDP response back
#it returns both the data and the details of the remote host and port.
data, addr = client.recvfrom(4096)

print(data)
client.close()