from rest_framework import serializers
from user.models import user
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields= ['FirstName','LasttName','UserName','Password']
