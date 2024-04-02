import socket

HOST = '127.0.0.1'
PORT = 65456

#tcp echo client
#well-known 서버의 소켓에 connect를 통해 연결 요청
#보낼때 순수 string을 utf-8 형식의 byte로 변환해서 보냄

print('> echo-client is activated')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
    clientSocket.connect((HOST, PORT))
    while True:
        sendMsg = input("> ")
        clientSocket.sendall(bytes(sendMsg, 'utf-8'))
        recvData = clientSocket.recv(1024)
        print('> received:', recvData.decode('utf-8'))
        if sendMsg == "quit":
            break

print('> echo-client is de-activated')