from concurrent import futures
import grpc
import logging
import serverA_pb2
import serverA_pb2_grpc

import serverB_pb2
import serverB_pb2_grpc

class Logger(serverB_pb2_grpc.LoggerServicer):
    def getLog(self, request, context):
        try:
            channel = grpc.insecure_channel('servera:80')
            stub = serverA_pb2_grpc.TimerStub(channel)
            res = stub.getTime(serverA_pb2.Request(name=request.name))
        except:
            res = None
        f = open('logs.txt', 'a')
        f.write(res.t)
        f.close()
        print(res.t)
        logging.info(res.t)       
        return serverB_pb2.Res(log=request.name+' on '+res.t)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    serverB_pb2_grpc.add_LoggerServicer_to_server(Logger(), server)
    server.add_insecure_port('[::]:50001')
    server.start()
    print("server start")    
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    print("start")
    # print(Logger.getLog(serverA_pb2.Request(name='test')))
    serve()
