import random
import time

import zmq

def main():
    ctx = zmq.Context()
    # SUB패턴으로 소켓을 열어 server측 publisher의 메시지를 받음
    subscriber = ctx.socket(zmq.SUB)
    # SUB패턴으로 메시지를 받을 때 모든 바이트 타입의 메시지를 수신하도록 설정, (공백으로 시작하는 모든 패턴에 대해 수신 = 모든 패턴에 대해 수신)
    subscriber.setsockopt(zmq.SUBSCRIBE, b'')
    subscriber.connect("tcp://localhost:5557")
    # PUSH패턴으로 소켓을 열어 server측 collector에게 메시지를 보냄
    publisher = ctx.socket(zmq.PUSH)
    publisher.connect("tcp://localhost:5558")
    
    
    random.seed(time.time())
    while True:
        # .poll()을 통해 100ms마다 주기적으로 수신 버퍼에 있는지 확인한다. 아니라면 일반적으로 0, 에러상황시 -1이 리턴됨
        # zmq.POLLIN은 수신 버퍼에 데이터가 있으면 true, 없으면 false인 flag임
        if subscriber.poll(100) & zmq.POLLIN:
            message = subscriber.recv()
            print("I: received message ", message)
        else:
            rand = random.randint(1, 100)
            if rand < 10:
                time.sleep(1)
                publisher.send(b"%d" % rand)
                print("I: sending message ", rand)
            
#전체적으로 client는 sub를 통해 받기도 하지만 push를 통해 server에게 메시지를 보내기도 함

if __name__ == '__main__':
    main()