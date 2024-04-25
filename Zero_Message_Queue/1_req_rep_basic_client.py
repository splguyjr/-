import zmq

#client는 zmq.Context()로 객체 생성하고 zmq.REQ패턴으로 소켓을 열고 connect를 통해 서버에 연결
#연속으로 두번 이상 send를 할 순 없음

context = zmq.Context()

print("Connecting to hello world server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#1부터 10까지의 번호의 request에 바이트 형태 'Hello'를 보내고 서버로 부터 'World'fmf dmdekqqkedk cnffur
#zmq는 byte형태로 통신하기 때문에 send(b'str')이나 send_string('str')형태로 보내주어야 함.
for request in range(10):
    print("Sending request %s ..." % request)
    
    socket.send_string('Hello')
    
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))