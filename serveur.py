import socket

# host and port to listen on
host = ''  # listen on all available interfaces
port = 12345

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific address and port
server_socket.bind((host, port))

# listen for incoming connections (maximum of 5 queued connections)
server_socket.listen(5)

print('Server listening on port', port)

while True:
    # wait for a client to connect
    client_socket, client_address = server_socket.accept()

    # print information about the connected client
    print('Received connection from', client_address)

    # receive data from the client in chunks
    data = b''
    while True:
        chunk = client_socket.recv(1024)
        if not chunk:
            break
        data += chunk

    # print the received data
    print('Received data:', data)

    # close the connection with the client
    client_socket.close()