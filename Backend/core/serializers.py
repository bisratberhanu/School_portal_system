from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from . import models


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = models.User
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'role', 'old_password']

    def perform_create(self, validated_data):
        username, role, password = validated_data['username'], validated_data['role'], validated_data['old_password']
        result = models.InitialUser.objects.filter(username=username, role=role, password=password)
        if not result:
            raise serializers.ValidationError({'error': 'Invalid credentials.'})
            
        user = super().perform_create(validated_data)
        return user
    

class InitialUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InitialUser
        fields = ['id', 'username', 'role', 'password']