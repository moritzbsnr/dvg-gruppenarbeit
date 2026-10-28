import os
import sys
from concurrent import futures

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "generated"))

import grpc
from grpc_reflection.v1alpha import reflection
import article_condition_serviceproto_pb2 as pb2
import article_condition_serviceproto_pb2_grpc as pb2_grpc
from service_impl import ArticleConditionService


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_ArticleConditionServiceServicer_to_server(
        ArticleConditionService(), server
    )

    service_names = (
        pb2.DESCRIPTOR.services_by_name["ArticleConditionService"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(service_names, server)

    server.add_insecure_port("[::]:9090")
    server.start()
    print("gRPC-Server läuft auf Port 9090")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()