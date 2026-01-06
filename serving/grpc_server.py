import grpc
from concurrent import futures


class RecommendationService:
    def Recommend(self, request, context):
        return {"recommendations": [1, 2, 3]}


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()