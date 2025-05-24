from rest_framework import serializers
from django.contrib.auth import authenticate
from user.models import User


class LoginSerializer(serializers.Serializer):
    """
    Serializer for login endpoint.
    """
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(username=attrs.get("username"),
                            password=attrs.get("password"))
        if user:
            attrs["user"] = user
            return super().validate(attrs) 
        raise serializers.ValidationError("Invalid username or password")


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

