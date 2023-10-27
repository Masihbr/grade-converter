from rest_framework import generics, permissions
from accounts import serializers as account_serializers


class UserSignUpAPIView(generics.CreateAPIView):
    serializer_class = account_serializers.UserSignUpSerializer
    permission_classes = [permissions.AllowAny]
