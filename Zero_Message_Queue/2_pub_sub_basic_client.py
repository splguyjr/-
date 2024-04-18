import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.SUB)#SUB패턴으로 socket 열고 connect

print("Collecting updates from weather server...")
socket.connect("tcp://localhost:5556")

#command입력을 통해 추가적으로 zip_filter를 설정해주거나 그렇지 않으면 10001이 default
zip_filter = sys.argv[1] if len(sys.argv) > 1 else "10001"
#setsockopt_string()을 사용해서 전달한 문자열을 인코딩한 값이 메시지의 첫부분에 해당할 때에만 메시지가 수신된다
#따라서 이 코드에선 zip_code에 해당하는 패턴이 앞에 나와야만 가능한 것
socket.setsockopt_string(zmq.SUBSCRIBE, zip_filter)

total_temp = 0
for update_nbr in range(100):
    string = socket.recv_string()
    zipcode, temperature, relhumidity = string.split()
    total_temp += int(temperature)
    
    print(f"zipcode: {zipcode}, temperature: {temperature}, relhumidity: {relhumidity}")
    
    """print("Receive temperature for zipcode "
          f"{zip_filter} was {temperature} F")
    
    print("Average temperature for zipcode "
          f"{zip_filter} was {total_temp/(update_nbr+1)} F")"""