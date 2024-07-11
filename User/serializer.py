from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken
from models import User


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=123, min_length=7, write_only=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'token']

    def get_token(self, user):
        tokens = AccessToken.for_user(user)
        token = str(tokens)
        return token


class UserSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=455)
    password = serializers.CharField(max_length=233, write_only=True)
    token = serializers.CharField(max_length=123, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError('An email address is required to log in.')

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.')
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.')

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.')

        tokens = AccessToken.for_user(user)
        token = str(tokens)
        return {
            'email', user.email,
            'tokens', token
        }

    class UserInfoSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = '__all__'
