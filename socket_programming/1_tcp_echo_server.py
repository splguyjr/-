import socket

HOST = '127.0.0.1'
PORT = 65456

#tcp echo server
#지정된 포트번호에 bind하고 client가 connect() 요청 보내오기를 listen()하고 있다가 accept()
#clientSocket은 server측에서 client와 통신하기 위해서 생성한 새로운 socket

print('> echo-server is activated')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
    serverSocket.bind((HOST, PORT))
    serverSocket.listen()
    clientSocket, clientAddress = serverSocket.accept()
    with clientSocket:
        print('> client connected by IP address {0} with Port number {1}'.format(clientAddress[0], clientAddress[1]))
        while True:
            RecvData = clientSocket.recv(1024)
            print('> echoed:', RecvData.decode('utf-8'))
            clientSocket.send(RecvData)
            if RecvData.decode('utf-8') == 'quit':
                break
            
print('> echo-server is de-activated')
            
    