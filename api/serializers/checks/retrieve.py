from rest_framework import serializers


class ServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()

class PropertiesSerializer(serializers.Serializer):
    deviceName = serializers.CharField(required=False)
    image = serializers.URLField(required=False)
    imei = serializers.CharField(required=False)
    meid = serializers.CharField(required=False)
    imei2 = serializers.CharField(required=False)
    serial = serializers.CharField(required=False)
    estPurchaseDate = serializers.IntegerField(required=False)
    simLock = serializers.BooleanField(required=False)
    replaced = serializers.BooleanField(required=False)
    warrantyStatus = serializers.CharField(required=False)
    refurbished = serializers.BooleanField(required=False)
    apple_region = serializers.CharField(source='apple/region', required=False)
    loaner = serializers.BooleanField(required=False)
    fmiOn = serializers.BooleanField(required=False)
    lostMode = serializers.BooleanField(required=False)

class RetrieveIMEICheckSerializer(serializers.Serializer):
    id = serializers.CharField()
    type = serializers.CharField()
    status = serializers.CharField()
    orderId = serializers.CharField(allow_null=True)
    service = ServiceSerializer()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    deviceId = serializers.CharField()
    processedAt = serializers.IntegerField()
    properties = serializers.JSONField(default=dict)
