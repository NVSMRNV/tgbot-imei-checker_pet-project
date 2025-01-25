from rest_framework import serializers


class RetriveIMEIServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=1)
    title = serializers.CharField(max_length=127)
    price = serializers.CharField(max_length=127)
