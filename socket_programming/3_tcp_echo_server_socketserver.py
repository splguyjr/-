import socketserver

#socketserver의 이미 구현되어있는 모듈을 활용해서 편하게 구현
#synchronous하기에 하나의 client가 연결이 끊겨야만 다른 client가 통신할 수 있다는 문제점
#클라이언트가 quit을 통해 연결을 종료해도 서버가 계속해서 server_forever하고 있기에 앞선 tcp_echo_server와는 다름
#하지만 한번에 사실상 하나의 클라이언트와만 통신할 수 있다는 점은 여전함

class MyTCPSocketHandler(socketserver.BaseRequestHandler):
    """
    서버를 위한 Request Handler
    
    한 connection당 한번 인스턴스화되는 객체이며,
    socketserver.BaseRequestHandler를 상속받기에
    handle() method를 override해서 구현해주어야 동작함.
    """
    
    def handle(self):
        print('> client connected by IP address {0} with Port number {1}'.format(self.client_address[0], self.client_address[1]))
        while True:
            RecvData = self.request.recv(1024)
            print('> echoed:', RecvData.decode('utf-8'))
            self.request.sendall(RecvData)
            if RecvData.decode('utf-8') == 'quit':
                break
        
if __name__ == "__main__":
    HOST, PORT = '127.0.0.1', 65456
    print('> echo-server is activated')
    #서버를 만들고 해당 서버의 소켓이 어떤 IP 주소와 Port번호를 쓸지 binding
    with socketserver.TCPServer((HOST, PORT), MyTCPSocketHandler) as server:
        server.serve_forever()
    print('> echo-server is de-activated')