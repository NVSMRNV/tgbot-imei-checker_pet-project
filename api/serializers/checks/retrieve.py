from rest_framework import serializers


class RetrieveIMEICheckPropertiesSerializer(serializers.Serializer):
    device_name = serializers.CharField(max_length=127)
    imei = serializers.CharField(max_length=127)


class RetrieveIMEICheckSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=127)
    status = serializers.CharField(max_length=127)
    properties = RetrieveIMEICheckPropertiesSerializer()
