import grpc
from concurrent import futures # a high-level interface for asynchronously executing callables, 서버에서 비동기적으로 여러 클라이언트 요청을 처리하기 위해 사용

import hello_grpc_pb2 # message class
import hello_grpc_pb2_grpc # client(MyServiceStub) & server class(MyServiceServicer)

import hello_grpc # 원격 호출될 함수를 import, import functions to be remotely called

# protoc가 생성한 Servicer 클래스를 base class로 두고 원격 호출될 함수들을 멤버로 갖는 서버 클래스 생성
class MyServiceServicer(hello_grpc_pb2_grpc.MyServiceServicer):
    
    # 서버 클래스에 원격 호출될 함수에 대한 rpc 함수를 작성함
    
    # proto 파일 내에 정의한 rpc 함수 이름에 대응하는 멤버 함수를 작성
    def MyFunction(self, request, context):
        # proto 파일 내 message 이름과 동일한 message class를 생성하여 응답 전달 용도로 사용
        response = hello_grpc_pb2.MyNumber()
        # 원격 호출될 함수 my_func에게 client로부터 받은 입력 파라미터를 전달하여 실행
        # 이후 message class의 변수(response.value)에 원격 함수의 수행 결과를 저장함
        response.value = hello_grpc.my_func(request.value)
        #원격 함수 호출 결과를 client에게 돌려줌
        return response

#grpc server 생성, ThreadPoolExecutor -> a pool of threads to execute calls asynchronously    
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# grpc.server에 직접 정의한 MyServiceServicer를 추가함
hello_grpc_pb2_grpc.add_MyServiceServicer_to_server(MyServiceServicer(), server)

# grpc.server의 통신 포트를 열고 start()로 서버를 실행함
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# grpc server가 유지되도록 프로그램 실행을 유지함
try:
    server.wait_for_termination()
except KeyboardInterrupt:
    server.stop(0)