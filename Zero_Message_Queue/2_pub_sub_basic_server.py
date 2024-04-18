import zmq
from random import randrange

print("Publishing updates at weather server...")

context = zmq.Context()
socket = context.socket(zmq.PUB)#PUB패턴으로 socket 열고 bind
socket.bind("tcp://*:5556")

while True:
    zipcode = randrange(1, 100000)
    temperature = randrange(-80, 135)
    relhumidity = randrange(10, 60)
    
    socket.send_string(f"{zipcode} {temperature} {relhumidity}")