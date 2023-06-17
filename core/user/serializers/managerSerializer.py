from django.db import IntegrityError
from django.forms import ValidationError
from rest_framework import serializers
from user.models import user
class managerSerializer(serializers.ModelSerializer):

    class Meta:
        model= user
        exclude = ['Group','is_staff']