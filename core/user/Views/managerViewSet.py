from rest_framework import viewsets,status
from rest_framework.response import Response
from user.models import userType
from user.utils.encryption import hashpassword
from user.models import user
from user.utils.tokenHandler import token as tk
from user.serializers.managerSerializer  import managerSerializer
from user.utils.pagination import MyPagination
from user.utils.filterclass import MyModelFilter
from rest_framework.exceptions import APIException
class managerViewsSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class=managerSerializer
    pagination_class = MyPagination
    filterset_class = MyModelFilter
    lookup_field = 'UserName'
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = managerSerializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            hashedPassword = hashpassword().hash(request.data['Password'])
            role = userType.objects.get(Type='user')
            serializer.save(Group=role, Password=hashedPassword)
            token = tk().createtokken(request.data.get('UserName'), 'user')
            return Response({"token": token}, status=status.HTTP_201_CREATED)
        except APIException as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except APIException as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
            