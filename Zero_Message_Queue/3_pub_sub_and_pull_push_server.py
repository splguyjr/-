import zmq

def main():
    ctx = zmq.Context()
    publisher = ctx.socket(zmq.PUB)
    publisher.bind("tcp://*:5557")
    collector = ctx.socket(zmq.PULL)
    collector.bind("tcp://*:5558")
    
    while True:
        message = collector.recv()
        print("I: publishing update ", message)
        publisher.send(message)
        
 #전체적으로 서버는 publisher를 통해 subscriber인 client에게 메시지를 보내기도 하고, collector를 통해서 메시지를 받기도 함.      
        
if __name__ == '__main__':
    main()