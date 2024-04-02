import socket

HOST = '127.0.0.1'
PORT = 65456

#client는 socket을 열고 bind되어있는 server의 소켓 주소에 connect()
#이후 sendall을 통해 msg를 보내고 echo되어오는 msg를 받음

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
        
        try:
            if clientSocket.connect((HOST, PORT)) == -1:
                print('> connect() failed and program terminated')
                clientSocket.close()
                return
        except Exception as exceptionObj:
            print('connect() failed by exception:', exceptionObj)
            return
        
        while True:
            sendMsg = input("> ")
            clientSocket.sendall(bytes(sendMsg, 'utf-8'))
            recvData = clientSocket.recv(1024)
            print('> received:', recvData.decode('utf-8')) #들어온 byte type msg를 다시 string utf-8로 decode
            if sendMsg == "quit":
                break
            
if __name__ == "__main__":
    print('> echo-client is activated')
    main()
    print('> echo client is de-activated')
            