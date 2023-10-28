from django.urls import path
from calculator import views

urlpatterns = [
    path('gpa/', views.CalculatorAPIView.as_view(), name='calculate-gpa'),
]
