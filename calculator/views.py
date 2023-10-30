from rest_framework import generics, permissions
from calculator.calculator import calculate_gpa
from rest_framework.response import Response


# Create your views here.
class CalculatorAPIView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    @staticmethod
    def post(request):
        return Response(calculate_gpa(request.data))
