from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()


class UserSignUpSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'student_id', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data: dict):
        user = User.objects.create_user(
            username=validated_data['username'], password=validated_data['password']
        )
        username = validated_data.pop('username')
        _ = validated_data.pop('password')
        User.objects.filter(username=username).update(**validated_data)
        user.refresh_from_db()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'password')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'student_id', 'first_name', 'last_name', 'email')
        read_only_fields = ('username',)
