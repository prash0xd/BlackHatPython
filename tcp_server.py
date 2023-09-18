import socket
import threading

#IP Address & port to listen on
IP = '0.0.0.0'
PORT = 9998

def main():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((IP,PORT))

    server.listen(5) #server starts listening with a maximum back-log connection of 5
    #back-log  represents the maximum number of pending connections that the operating system is willing to queue up for server application to accept.
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        client, address = server.accept()  #client socket in the client variable & remote connection details in address variable
        # accept() is called, it dequeues the oldest connection request from the backlog and creates a new socket for communication with that client.
        print(f'[*] Accepted connection from {address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client,args=(client,)) #new thread object that points to handle_client function, pass in client socket object as an argument
        client_handler.start() #start the thread to handle incoming new connections

def handle_client(client_socket):
    with client_socket as socket:
        request = sock.recv(1024) #recive request from client
        print(f'[*] Request {request.decode("utf-8")}')
        sock.send(b'ACK')  #sends message back to client

if __name__ == '__main__':
    main()