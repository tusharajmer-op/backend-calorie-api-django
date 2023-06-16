from django_filters import rest_framework as filters
from user.models import user

class MyModelFilter(filters.FilterSet):
    UserName = filters.CharFilter(lookup_expr='icontains')
    CreatedOn = filters.DateFilter()

    class Meta:
        model = user
        fields = ['UserName', 'CreatedOn']
