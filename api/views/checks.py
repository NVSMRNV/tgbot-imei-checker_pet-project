from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from api.services.checks.create import CreateIMEICheckservice
from api.serializers.checks.retrieve import RetrieveIMEICheckSerializer


class CreateIMEICheckAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request, *args, **kwargs) -> Response:
        output = CreateIMEICheckservice(request.data).process()
        if output.result:
            serializer = RetrieveIMEICheckSerializer(output.result)
            return Response(serializer.data, status=output.response_status)
        return Response(output.errors, status=output.response_status)
