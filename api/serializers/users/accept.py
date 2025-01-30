from rest_framework import serializers

from api.models.whitelist import WhiteList


class AcceptUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhiteList
        fields = '__all__'
    