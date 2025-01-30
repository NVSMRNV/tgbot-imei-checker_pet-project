from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from api.serializers.users.accept import AcceptUserSerializer
from api.serializers.users.retrieve import RetrieveUserSerializer

from api.services.users.accept import AcceptUserService
from api.services.users.create import CreateUserService
from api.services.users.current import CurrentUserService


class ListCreateUserAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request: Request, *args, **kwargs) -> Response:
        output = CreateUserService(request.data).process()
        if output.result:   
            serializer = RetrieveUserSerializer(output.result)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(output.errors, status=output.response_status)

    def get(self, request: Request, *args, **kwargs) -> Response:
        output = CurrentUserService(
            {'uid': request.query_params.get('uid')}
        ).process()
        if output.result:   
            serializer = RetrieveUserSerializer(output.result)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(output.errors, status=output.response_status)
    

class AcceptUserAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request: Request, *args, **kwargs) -> Response:
        output = AcceptUserService(
            {'uid': request.query_params.get('uid')}
        ).process()
        if output.result:   
            serializer = AcceptUserSerializer(output.result)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(output.errors, status=output.response_status)
