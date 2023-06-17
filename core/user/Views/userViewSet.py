from rest_framework import viewsets,status
from rest_framework.response import Response
from user.models import user,userType
from user.serializers.userSerializer import userSerializer 
from user.utils.tokenHandler import token as tk
from user.utils.encryption import hashpassword
from rest_framework.exceptions import APIException
class userView(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userSerializer
    lookup_field = 'UserName'
    def list(self, request, *args, **kwargs):
        return Response([])
    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data)
        except APIException as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
        
    def create(self, request, *args, **kwargs):
        try:
            serializer = userSerializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            hashedPassword = hashpassword().hash(request.data['Password'])
            role = userType.objects.get(Type='user')
            serializer.save(Group=role, Password=hashedPassword)
            token = tk().createtokken(request.data.get('UserName'), 'user')
            return Response({"token": token}, status=status.HTTP_201_CREATED)
        except APIException as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
        