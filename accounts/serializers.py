from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import UserProfile
from .models import User

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    recommendations = serializers.CharField(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'

