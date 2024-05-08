import grpc

import hello_grpc_pb2
import hello_grpc_pb2_grpc

# gRPC 통신 채널을 생성함
channel = grpc.insecure_channel('localhost:50051')

# protoc가 생성한 _pb2_grpc파일의 MyServicestub 함수를 channel을 사용하여 실행하여 stub을 생성함
stub = hello_grpc_pb2_grpc.MyServiceStub(channel)

# protoc가 생성항 _pb2 파일의 메시지 타입에 맞춰서, 원격 함수에 전달할 메시지를 만들고, 전달할 값을 저장함
request = hello_grpc_pb2.MyNumber(value=4)

# 원격 함수를 stub을 사용하여 호출(MyNumber타입의 request를 파라미터로 넣어)
response = stub.MyFunction(request)

# server가 처리해준 원격 함수의 결과를 출력함
print("gRPC result:", response.value)
