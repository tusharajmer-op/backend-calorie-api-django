from rest_framework import viewsets,status
from rest_framework.response import Response
from user.models import user,userType
from user.indexserailizer import serializers
from user.utils.tokenHandler import token as tk
from user.utils.encryption import hashpassword
class userView(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = serializers().userSerializer
    lookup_field = 'UserName'
    def list(self, request, *args, **kwargs):
        return Response([])
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def create(self, request, *args, **kwargs):
        data= {key: value for key, value in request.data.items()}
        print(request.data['Password'])
        hashedPassword = hashpassword().hash(request.data['Password'])
        print(hashedPassword)
        serializer = serializers().userSerializer(data=request.data,context={'request':request})
        if serializer.is_valid():
            role = userType.objects.get(Type='user')
            instance = serializer.save(Group = role,Password = hashedPassword)
            token = tk().createtokken(request.data.get('UserName'),'user')
            return Response({"token":token},status=status.HTTP_201_CREATED)
            