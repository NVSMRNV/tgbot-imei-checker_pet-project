from rest_framework import serializers

from api.models.users import User


class RetrieveUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    