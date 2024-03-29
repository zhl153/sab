import grpc
import serverB_pb2
import serverB_pb2_grpc
import time

def run():
    with grpc.insecure_channel('35.184.122.11:80') as channel:
        stub = serverB_pb2_grpc.LoggerStub(channel)
        response = stub.getLog(serverB_pb2.Req(name='Client'))
        print(response.log)

if __name__ == '__main__':
    while True:
        run()
        time.sleep(2)
