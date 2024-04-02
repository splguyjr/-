import socket

HOST = '127.0.0.1'
PORT = 65456

#bind가 실패했을 때 출력후 socket 닫고 어떠한 exception인지 출력하고 종료

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
        try:
            if serverSocket.bind((HOST, PORT)) == -1:
                print('> bind() failed and program terminated')
                serverSocket.close()
                return
        except Exception as exceptionObj:
            print('> bind() failed by exception:', exceptionObj)
            serverSocket.close()
            return

        if serverSocket.listen() == -1:
            print('> listen() failed and program terminated')
            serverSocket.close()
            return
        
        clientSocket, clientAddress = serverSocket.accept()
        
        with clientSocket:
            print('> client connected by IP address {0} with Port number {1}'.format(clientAddress[0], clientAddress[1]))
            while True:
                RecvData = clientSocket.recv(1024)
                print('> echoed:', RecvData.decode('utf-8'))
                clientSocket.sendall(RecvData)
                if RecvData.decode('utf-8') == 'quit':
                    break
                
if __name__ == "__main__":
    print('> echo-server is activated')
    main()
    print('> echo-server is de-activated')