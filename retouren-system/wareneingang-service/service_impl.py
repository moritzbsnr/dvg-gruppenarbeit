import article_condition_serviceproto_pb2 as pb2
import article_condition_serviceproto_pb2_grpc as pb2_grpc
import grpc


class ArticleConditionService(pb2_grpc.ArticleConditionServiceServicer):
    def __init__(self):
        self.results = {}  # TODO: Speicher für Prüfergebnisse

    def CheckCondition(self, request, context):
        # TODO: Entscheidungslogik
        return pb2.ConditionCheckResponse(
            return_id=request.return_id,
            sku=request.sku,
            decision=pb2.MANUAL_REVIEW,
            reason="TODO: noch nicht implementiert",
            requires_manual_review=True,
        )

    def CheckConditionBatch(self, request, context):
        # TODO: über request.items iterieren
        return pb2.ConditionCheckBatchResponse(results=[])

    def GetCheckResult(self, request, context):
        # TODO: gespeichertes Ergebnis zurückgeben
        context.abort(grpc.StatusCode.NOT_FOUND, "TODO: noch nicht implementiert")