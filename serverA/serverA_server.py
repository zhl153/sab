import grpc
import logging
import serverA_pb2
import serverA_pb2_grpc
import datetime
from concurrent import futures

class Timer(serverA_pb2_grpc.TimerServicer):
    def getTime(self, request, context):
        f = open('log.txt', 'a')
        f.write('got request from ' + request.name)
        print('got request from ' + request.name)
        logging.info('got a request from ' + request.name)
        f.close()
        return serverA_pb2.Response(t=str(datetime.datetime.now()))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    serverA_pb2_grpc.add_TimerServicer_to_server(Timer(), server)
    server.add_insecure_port('[::]:50000')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
