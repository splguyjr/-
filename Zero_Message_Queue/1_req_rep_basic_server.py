import time
import zmq

#zmq.Context()로 객체 생성이후, zmq.REP패턴의 소켓을 열고 tcp://*:5555에 bind

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #client로부터의 request를 기다림
    message = socket.recv()
    print("Received request: %s" % message)
    

    time.sleep(1)
    
    socket.send(b"World")