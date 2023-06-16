from rest_framework import serializers
from user.models import userType
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = userType
        fields= '__all__'