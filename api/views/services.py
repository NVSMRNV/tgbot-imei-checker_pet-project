from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from api.services.services.list import ListIMEIServiceService
from api.serializers.services.retrieve import RetriveIMEIServiceSerializer


class ListIMEIServiceAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request: Request, *args, **kwargs) -> Response:
        output = ListIMEIServiceService(request.data).process()
        if output.result:
            serializer = RetriveIMEIServiceSerializer(output.result, many=True)
            return Response(serializer.data, status=output.response_status)
        return Response(output.errors, status=output.response_status)
