from rest_framework import generics, permissions, status
from rest_framework.response import Response
from accounts import serializers as account_serializers
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login


class UserSignUpAPIView(generics.CreateAPIView):
    serializer_class = account_serializers.UserSignUpSerializer
    permission_classes = [permissions.AllowAny]


class LoginAPIView(generics.GenericAPIView):
    serializer_class = account_serializers.UserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            request=request,
            username=serializer.validated_data.get("username"),
            password=serializer.validated_data.get("password"),
        )
        if user is not None:
            auth_login(request, user)
            return Response({"detail": "Logged in successfully."})
        else:
            return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
