from rest_framework import serializers
from user.utils.errors import InvalidRequestType
from user.models import user
class userSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = user
        fields= ['FirstName','LasttName','UserName','Password']
    def validate(self, attrs):
        print("hello")
        raise InvalidRequestType("Invalid Request Type")
    
