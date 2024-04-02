import socketserver
import threading

#파이썬은 원래 하나의 부모만 가질 수 있으나 mix-In 클래스를 활용
#mix-in 클래스가 먼저 오고 뒤에 오는 부모 클래스의 method들을 override
#threading 모듈안에 request가 왔을 때 main thread에서 새로운 thread를 생성해 handle하도록 하는 처리
class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        print('> client connected by IP address {0} with Port number {1}'.format(self.client_address[0], self.client_address[1]))
        
        while True:
            RecvData = self.request.recv(1024)
            cur_thread = threading.current_thread() #request를 handle 할때마다, 즉 새로운 client 연결마다 thread가 생성되어 처리되는 것을 확인
            print('> echoed:', RecvData.decode('utf-8'), 'by', cur_thread.name)
            self.request.sendall(RecvData)
            if RecvData.decode('utf-8') == 'quit':
                break


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = "localhost", 65456
    print('> echo-server is activated')
    
    with ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler) as server:
     #   ip, port = server.server_address
        
        server_thread = threading.Thread(target=server.serve_forever)
        
        server_thread.daemon = True
        server_thread.start()
        print('> server loop running in thread (main thread):', server_thread.name)
        
        
        baseThreadNumber = threading.active_count()
        while True:
            msg = input('> ')
            if msg == 'quit':
                if baseThreadNumber == threading.active_count():
                    print('> stop procedure started')
                    break
                else:
                    print('> active threads are remaining :', threading.active_count() - baseThreadNumber, 'threads')
    
        print('> echo-server is de-activated')
        server.shutdown()
        
        
    